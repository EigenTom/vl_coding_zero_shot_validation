#!/usr/bin/env python3
"""
Download ChartCoder model weights from HuggingFace.

Downloads xxxllz/ChartCoder (7B, BF16) to a local directory so that
serve_chartcoder.py can load it without network access at inference time.

Supports HF_ENDPOINT env var for mirror fallback (e.g. https://hf-mirror.com).

Usage:
  uv run python setup/download_chartcoder.py
  uv run python setup/download_chartcoder.py --output ./models/ChartCoder
  HF_ENDPOINT=https://hf-mirror.com uv run python setup/download_chartcoder.py
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download ChartCoder model weights from HuggingFace",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--output", default="./models/ChartCoder",
                        help="Local directory to save model weights")
    parser.add_argument("--repo-id", default="xxxllz/ChartCoder",
                        help="HuggingFace model repository ID")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        logging.error("huggingface_hub not installed. Run: uv pip install huggingface_hub")
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    logging.info("=" * 60)
    logging.info("Downloading %s", args.repo_id)
    logging.info("HF endpoint : %s", endpoint)
    logging.info("Local dir   : %s", output_dir.resolve())
    logging.info("Model size  : ~7B params, BF16 — ensure sufficient disk space (~15 GB)")
    logging.info("=" * 60)

    try:
        path = snapshot_download(
            repo_id=args.repo_id,
            local_dir=str(output_dir),
            local_dir_use_symlinks=False,
        )
        logging.info("=" * 60)
        logging.info("DONE  saved to: %s", path)
        logging.info("=" * 60)
    except Exception as exc:
        logging.error("Download failed: %s", exc)
        logging.error("If HuggingFace is inaccessible, retry with:")
        logging.error("  HF_ENDPOINT=https://hf-mirror.com uv run python setup/download_chartcoder.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
