#!/usr/bin/env python3
"""
Download ChartMimic benchmark from HuggingFace and save as JSONL.

Downloads the ChartMimic/ChartMimic dataset, filters to the image-to-code
task, and saves each sample as a JSON line with base64-encoded images.

Usage:
  uv run python setup/download_chartmimic.py
  uv run python setup/download_chartmimic.py --output ./data/chartmimic --split test
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import logging
import sys
from pathlib import Path
from typing import Any

from PIL import Image


def pil_to_b64(img: Any, fmt: str = "PNG") -> str:
    """Convert a PIL Image to a base64-encoded string."""
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format=fmt)
    return base64.b64encode(buf.getvalue()).decode()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download ChartMimic benchmark and save as JSONL",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--output", default="./data/chartmimic",
                        help="Directory to save the output JSONL file")
    parser.add_argument("--split", default="test",
                        help="Dataset split to download")
    parser.add_argument("--task-filter", default="image-to-code",
                        help="Filter to this Task value (empty string = no filter)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    try:
        from datasets import load_dataset
    except ImportError:
        logging.error("datasets not installed. Run: uv pip install datasets")
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "test.jsonl"

    logging.info("=" * 60)
    logging.info("Downloading ChartMimic/ChartMimic  split=%s", args.split)
    if args.task_filter:
        logging.info("Task filter: %s", args.task_filter)
    logging.info("Output: %s", output_path)
    logging.info("=" * 60)

    ds = load_dataset("ChartMimic/ChartMimic", split=args.split, trust_remote_code=True)
    logging.info("Total rows in split: %d", len(ds))

    # Filter to image-to-code task
    if args.task_filter:
        ds = ds.filter(lambda row: row["Task"] == args.task_filter)
        logging.info("Rows after task filter ('%s'): %d", args.task_filter, len(ds))

    n_written = 0
    n_skipped = 0

    with open(output_path, "w", encoding="utf-8") as f:
        for i, row in enumerate(ds):
            try:
                # Input chart image (what the model receives)
                input_img = row.get("InputFigurePreview")
                if input_img is None:
                    logging.warning("Row %d: missing InputFigurePreview — skipping", i)
                    n_skipped += 1
                    continue
                if not isinstance(input_img, Image.Image):
                    input_img = Image.fromarray(input_img)

                # Ground truth chart image (used for SSIM evaluation)
                gt_img = row.get("GroundTruthFigurePreview")
                if gt_img is None:
                    logging.warning("Row %d: missing GroundTruthFigurePreview — skipping", i)
                    n_skipped += 1
                    continue
                if not isinstance(gt_img, Image.Image):
                    gt_img = Image.fromarray(gt_img)

                # Ground truth code
                gt_code = row.get("GroundTruthFigureCode", "")
                if not gt_code:
                    logging.warning("Row %d: missing GroundTruthFigureCode — skipping", i)
                    n_skipped += 1
                    continue

                record = {
                    "example_id":      row.get("ExampleID", f"sample_{i:04d}"),
                    "task":            row.get("Task", ""),
                    "input_image_b64": pil_to_b64(input_img),
                    "gt_code":         gt_code,
                    "gt_image_b64":    pil_to_b64(gt_img),
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                n_written += 1

                if (i + 1) % 50 == 0:
                    logging.info("  Processed %d / %d rows  (written=%d  skipped=%d)",
                                 i + 1, len(ds), n_written, n_skipped)

            except Exception as exc:
                logging.warning("Row %d: error (%s) — skipping", i, exc)
                n_skipped += 1

    logging.info("=" * 60)
    logging.info("DONE  written=%d  skipped=%d", n_written, n_skipped)
    logging.info("Output: %s", output_path)
    logging.info("=" * 60)


if __name__ == "__main__":
    main()
