#!/usr/bin/env python3
"""
ChartCoder OpenAI-Compatible Inference Server.

Wraps ChartCoder (xxxllz/ChartCoder, 7B LLaVA-DeepSeekCoder) behind a FastAPI
server that exposes a POST /v1/chat/completions endpoint in the standard
OpenAI multimodal format.  This lets the rest of the validation pipeline
treat ChartCoder exactly like any vLLM-served model.

IMPORTANT: Run this script in the chartcoder_env conda environment where
ChartCoder's dependencies are installed (torch==2.0.1, transformers==4.31.0).
The main project environment does NOT need these pinned deps.

Setup (one-time):
  git clone https://github.com/thunlp/ChartCoder.git ./ChartCoder
  conda create -n chartcoder_env python=3.10 -y
  conda activate chartcoder_env
  pip install -e ./ChartCoder
  pip install fastapi "uvicorn[standard]"

Usage:
  conda activate chartcoder_env
  python serve/serve_chartcoder.py \\
    --model-path ./models/ChartCoder \\
    --chartcoder-repo ./ChartCoder \\
    --port 8080
"""

from __future__ import annotations

import argparse
import base64
import io
import logging
import sys
import time
from pathlib import Path
from typing import Any

import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image

# ---------------------------------------------------------------------------
# Global model state (loaded once at startup)
# ---------------------------------------------------------------------------
_tokenizer = None
_model = None
_image_processor = None
_context_len = None

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI(title="ChartCoder OpenAI-Compatible API", version="1.0")


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------
def _load_model(model_path: str, chartcoder_repo: str) -> None:
    global _tokenizer, _model, _image_processor, _context_len

    # Add ChartCoder source to Python path so we can import llava.*
    repo = Path(chartcoder_repo).resolve()
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))

    from llava.model.builder import load_pretrained_model  # noqa: PLC0415

    logging.info("Loading ChartCoder from %s …", model_path)
    _tokenizer, _model, _image_processor, _context_len = load_pretrained_model(
        model_path=model_path,
        model_base=None,
        model_name="llava_deepseekcoder",
        device_map="auto",
    )
    _model.eval()
    logging.info("ChartCoder loaded  context_len=%s  device=%s",
                 _context_len, next(_model.parameters()).device)


# ---------------------------------------------------------------------------
# Inference helper
# ---------------------------------------------------------------------------
def _run_inference(
    text: str,
    image_pil: Image.Image | None,
    max_new_tokens: int,
    temperature: float,
    top_p: float,
) -> str:
    """Run a single forward pass and return the decoded output string."""
    from llava.constants import DEFAULT_IMAGE_TOKEN, IMAGE_TOKEN_INDEX  # noqa: PLC0415
    from llava.mm_utils import process_images, tokenizer_image_token     # noqa: PLC0415

    # Build prompt the same way as ChartCoder/inference.py — plain string, no conv_templates
    if image_pil is not None:
        prompt = f"### Instruction:\n{DEFAULT_IMAGE_TOKEN}\n{text}\n### Response:\n"
    else:
        prompt = f"### Instruction:\n{text}\n### Response:\n"

    input_ids = tokenizer_image_token(
        prompt, _tokenizer, IMAGE_TOKEN_INDEX, return_tensors="pt"
    ).unsqueeze(0).to(_model.device)

    # Process image — take index [0] to get a single tensor, then unsqueeze for batch dim
    if image_pil is not None:
        image_tensor = process_images([image_pil], _image_processor, _model.config)[0]
        image_tensor = image_tensor.unsqueeze(0).half().to(_model.device)
        image_sizes = [image_pil.size]
    else:
        image_tensor = None
        image_sizes = None

    # Generate
    gen_kwargs: dict[str, Any] = {
        "images": image_tensor,
        "image_sizes": image_sizes,
        "max_new_tokens": max_new_tokens,
        "use_cache": True,
    }
    if temperature > 0:
        gen_kwargs["do_sample"] = True
        gen_kwargs["temperature"] = temperature
        gen_kwargs["top_p"] = top_p
    else:
        gen_kwargs["do_sample"] = False

    with torch.inference_mode():
        output_ids = _model.generate(input_ids, **gen_kwargs)

    output_text = _tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
    return output_text


# ---------------------------------------------------------------------------
# OpenAI-compatible endpoint
# ---------------------------------------------------------------------------
@app.post("/v1/chat/completions")
async def chat_completions(request: dict) -> JSONResponse:
    if _model is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")

    messages = request.get("messages", [])
    max_tokens  = int(request.get("max_tokens", 2048))
    temperature = float(request.get("temperature", 0.1))
    top_p       = float(request.get("top_p", 0.95))

    # Find the last user message
    user_msg = None
    for msg in reversed(messages):
        if msg.get("role") == "user":
            user_msg = msg
            break
    if user_msg is None:
        raise HTTPException(status_code=400, detail="No user message in request")

    # Parse content: may be a plain string or a list of content parts
    content = user_msg["content"]
    text: str = ""
    image_pil: Image.Image | None = None

    if isinstance(content, str):
        text = content
    elif isinstance(content, list):
        for part in content:
            ptype = part.get("type", "")
            if ptype == "text":
                text += part.get("text", "")
            elif ptype == "image_url":
                url = part.get("image_url", {}).get("url", "")
                if url.startswith("data:image"):
                    # data:<mime>;base64,<data>
                    b64_data = url.split(",", 1)[1]
                    img_bytes = base64.b64decode(b64_data)
                    image_pil = Image.open(io.BytesIO(img_bytes)).convert("RGB")
                    # Use the first image only (ChartCoder is single-image)
                    break

    # Run inference
    try:
        output_text = _run_inference(
            text=text,
            image_pil=image_pil,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
    except Exception as exc:
        logging.exception("Inference error: %s", exc)
        raise HTTPException(status_code=500, detail=f"Inference error: {exc}") from exc

    # Return OpenAI-compatible response envelope
    return JSONResponse({
        "id": f"chatcmpl-{int(time.time() * 1000)}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "ChartCoder",
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": output_text},
            "finish_reason": "stop",
        }],
        "usage": {
            "prompt_tokens": -1,
            "completion_tokens": -1,
            "total_tokens": -1,
        },
    })


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "model_loaded": _model is not None}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve ChartCoder as an OpenAI-compatible API",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--model-path",       default="./models/ChartCoder",
                        help="Path to downloaded ChartCoder model directory")
    parser.add_argument("--chartcoder-repo",  default="./ChartCoder",
                        help="Path to cloned ChartCoder repository (for llava imports)")
    parser.add_argument("--port",             type=int, default=8080)
    parser.add_argument("--host",             default="0.0.0.0")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logging.info("=" * 60)
    logging.info("ChartCoder Server")
    logging.info("Model path     : %s", args.model_path)
    logging.info("ChartCoder repo: %s", args.chartcoder_repo)
    logging.info("Endpoint       : http://%s:%d/v1/chat/completions", args.host, args.port)
    logging.info("=" * 60)

    _load_model(args.model_path, args.chartcoder_repo)

    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
