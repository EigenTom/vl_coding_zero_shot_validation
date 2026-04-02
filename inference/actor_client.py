"""
Actor model HTTP client.

Sends requests to an OpenAI Chat Completions-compatible API endpoint
(either the ChartCoder FastAPI server or any vLLM-served model).

Two call types:
  generate() — initial code generation from a chart image
  refine()   — code refinement given previous code + critic's feedback text
               (target image is re-sent for visual context)

Retry logic and proxy-clearing follow the same pattern as vincicoder_repurpose.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any


# ---------------------------------------------------------------------------
# Utility: clear HTTP proxies before every outbound request
# (avoids 403 / Timeout in certain container environments)
# ---------------------------------------------------------------------------
def _clear_proxies() -> None:
    for key in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"):
        os.environ.pop(key, None)


# ---------------------------------------------------------------------------
# Internal shared implementation
# ---------------------------------------------------------------------------
def _post(
    url: str,
    model_id: str,
    messages: list[dict],
    params: dict,
    timeout: int = 120,
    max_retries: int = 3,
) -> str | None:
    """POST a chat-completions request and return the assistant content string."""
    try:
        import httpx
    except ImportError:
        raise RuntimeError("httpx required: uv pip install httpx")

    endpoint = f"{url.rstrip('/')}/v1/chat/completions"
    payload: dict[str, Any] = {
        "model":       model_id,
        "messages":    messages,
        "max_tokens":  params.get("max_tokens", 2048),
        "temperature": params.get("temperature", 0.1),
        "top_p":       params.get("top_p", 0.95),
    }
    # Forward any extra params (top_k, min_p, etc.) that vLLM accepts
    for key in ("top_k", "min_p", "presence_penalty", "repetition_penalty"):
        if key in params:
            payload[key] = params[key]

    api_key = os.environ.get("ACTOR_API_KEY", "sk-123456")

    for attempt in range(max_retries + 1):
        _clear_proxies()
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.post(
                    endpoint,
                    json=payload,
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
            logging.warning("[Actor] attempt %d/%d failed: %s",
                            attempt + 1, max_retries + 1, exc)
            if attempt < max_retries:
                time.sleep(2.0 * (attempt + 1))
    return None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def generate(
    target_image_b64: str,
    cfg: dict,
) -> str | None:
    """
    Initial chart-to-code generation.

    Sends the target chart image + the actor_initial prompt from config.
    Returns the raw model response string (expected to be Python code).
    """
    prompt_text = cfg["prompts"]["actor_initial"].strip()
    actor_cfg   = cfg["actor"]
    params      = cfg["actor_params"]

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_text},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{target_image_b64}"}},
            ],
        }
    ]

    return _post(
        url=actor_cfg["url"],
        model_id=actor_cfg["model_id"],
        messages=messages,
        params=params,
    )


def refine(
    target_image_b64: str,
    previous_code: str,
    critic_feedback: str,
    cfg: dict,
) -> str | None:
    """
    Code refinement given critic feedback.

    Sends:
      [text]    actor_refine prompt with {previous_code} and {critic_feedback} filled in
      [image]   the original target chart (for visual reference)

    Returns the raw model response string (expected to be corrected Python code).
    """
    refine_template = cfg["prompts"]["actor_refine"]
    prompt_text = refine_template.format(
        previous_code=previous_code,
        critic_feedback=critic_feedback,
    ).strip()

    actor_cfg = cfg["actor"]
    params    = cfg["actor_params"]

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_text},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{target_image_b64}"}},
            ],
        }
    ]

    return _post(
        url=actor_cfg["url"],
        model_id=actor_cfg["model_id"],
        messages=messages,
        params=params,
    )
