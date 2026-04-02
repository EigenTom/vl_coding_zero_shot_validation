"""
Critic model HTTP client.

Sends requests to an OpenAI Chat Completions-compatible vLLM endpoint
(Qwen3.5-122B-A10B or any compatible VLM).

The critic receives TWO images (current rendering + target chart) and NO code.
It returns either the single word "DONE" or a natural-language description of
the visual differences that the actor should fix.

Retry logic and proxy-clearing follow the same pattern as vincicoder_repurpose.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any


# ---------------------------------------------------------------------------
# Utility: clear HTTP proxies before every outbound request
# ---------------------------------------------------------------------------
def _clear_proxies() -> None:
    for key in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"):
        os.environ.pop(key, None)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def evaluate(
    current_image_b64: str,
    target_image_b64: str,
    cfg: dict,
) -> str | None:
    """
    Visual critic evaluation.

    Sends [IMAGE 1] = current rendering, [IMAGE 2] = target chart.
    Returns:
      - "DONE" if the critic judges the charts visually equivalent
      - A natural-language description of differences (actionable feedback)
      - None if the API call fails after all retries
    """
    try:
        import httpx
    except ImportError:
        raise RuntimeError("httpx required: uv pip install httpx")

    critic_cfg  = cfg["critic"]
    params      = cfg["critic_params"]
    system_text = cfg["prompts"]["critic_system"].strip()
    user_text   = cfg["prompts"]["critic_user"].strip()

    url      = f"{critic_cfg['url'].rstrip('/')}/v1/chat/completions"
    model_id = critic_cfg["model_id"]
    api_key  = os.environ.get("CRITIC_API_KEY", "sk-123456")

    payload: dict[str, Any] = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_text},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    # IMAGE 1: current rendering
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/png;base64,{current_image_b64}"}},
                    # IMAGE 2: target chart
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/png;base64,{target_image_b64}"}},
                ],
            },
        ],
        "max_tokens":  params.get("max_tokens", 1024),
        "temperature": params.get("temperature", 0.6),
        "top_p":       params.get("top_p", 0.95),
    }
    # Forward vLLM-specific params
    for key in ("top_k", "min_p", "presence_penalty", "repetition_penalty"):
        if key in params:
            payload[key] = params[key]

    max_retries = 3
    for attempt in range(max_retries + 1):
        _clear_proxies()
        try:
            with httpx.Client(timeout=120) as client:
                resp = client.post(
                    url, json=payload,
                    headers={"Authorization": f"Bearer {api_key}"},
                )
                resp.raise_for_status()
                data = resp.json()
            content = (
                data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "")
                    .strip()
            )
            return content or None
        except Exception as exc:
            logging.warning("[Critic] attempt %d/%d failed: %s",
                            attempt + 1, max_retries + 1, exc)
            if attempt < max_retries:
                time.sleep(2.0 * (attempt + 1))
    return None
