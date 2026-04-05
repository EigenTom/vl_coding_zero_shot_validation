#!/usr/bin/env python3
"""
Prepare ChartMimic benchmark data from the ICLR supplementary material.

Reads Python scripts from the ChartMimic supplementary material (direct_600
split), renders each script to PNG using subprocess + Agg backend, and saves a
JSONL file with the rendered image and GT code path for downstream evaluation.

The supplementary material must already be extracted.  Default location:
  /data/yilu/chartmimic_supp/ChartMimic/

Output JSONL format (one JSON object per line):
  {
    "example_id":      "bar_3",
    "gt_code":         "<full Python source>",
    "gt_py_path":      "/abs/path/to/bar_3.py",     # used by ChartMimic evaluators
    "input_image_b64": "<base64-encoded PNG>"        # GT rendering = actor input image
  }

Usage:
  # From the repo root:
  uv run python setup/download_chartmimic.py
  uv run python setup/download_chartmimic.py --supp-dir /data/yilu/chartmimic_supp/ChartMimic
  uv run python setup/download_chartmimic.py --num-samples 50   # quick test
"""

from __future__ import annotations

import argparse
import base64
import json
import logging
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Allow running as `python setup/download_chartmimic.py` from the repo root
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from inference.render import render_chart_code


_DEFAULT_SUPP_DIR = "/data/yilu/chartmimic_supp/ChartMimic"
_DEFAULT_SPLIT    = "direct_600"
_DEFAULT_OUTPUT   = "./data/chartmimic/test.jsonl"

_RENDER_CFG = {
    "timeout_sec":   60,    # GT scripts are well-formed but some are slow
    "output_format": "png",
    "bbox_inches":   "tight",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare ChartMimic benchmark data from supplementary material",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--supp-dir",
        default=_DEFAULT_SUPP_DIR,
        help="Path to the extracted ChartMimic supplementary material root",
    )
    parser.add_argument(
        "--split",
        default=_DEFAULT_SPLIT,
        choices=["direct_600", "customized_600", "direct_1800", "customized_1800"],
        help="Which dataset split to use",
    )
    parser.add_argument(
        "--output",
        default=_DEFAULT_OUTPUT,
        help="Output JSONL path",
    )
    parser.add_argument(
        "--num-samples",
        type=int,
        default=-1,
        help="Maximum number of samples to process (-1 = all)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    supp_dir   = Path(args.supp_dir)
    dataset_dir = supp_dir / "dataset" / args.split

    if not dataset_dir.exists():
        logging.error("Dataset directory not found: %s", dataset_dir)
        sys.exit(1)

    py_files = sorted(dataset_dir.glob("*.py"))
    if not py_files:
        logging.error("No .py files found in %s", dataset_dir)
        sys.exit(1)

    if args.num_samples > 0:
        py_files = py_files[: args.num_samples]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    logging.info("=" * 60)
    logging.info("ChartMimic data preparation")
    logging.info("  Split:       %s (%d scripts)", args.split, len(py_files))
    logging.info("  Dataset dir: %s", dataset_dir)
    logging.info("  Output:      %s", output_path)
    logging.info("=" * 60)

    n_written = 0
    n_failed  = 0

    with open(output_path, "w", encoding="utf-8") as out_f:
        for i, py_path in enumerate(py_files):
            example_id = py_path.stem          # e.g. "bar_3"
            gt_code    = py_path.read_text(encoding="utf-8")

            # Render GT code to PNG (this IS the input image the actor receives)
            png_bytes = render_chart_code(gt_code, _RENDER_CFG)
            if png_bytes is None:
                logging.warning(
                    "[%d/%d] %s — render FAILED, skipping",
                    i + 1, len(py_files), example_id,
                )
                n_failed += 1
                continue

            record = {
                "example_id":      example_id,
                "gt_code":         gt_code,
                "gt_py_path":      str(py_path.resolve().relative_to(_ROOT)),
                "input_image_b64": base64.b64encode(png_bytes).decode(),
            }
            out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
            n_written += 1

            if (i + 1) % 50 == 0 or (i + 1) == len(py_files):
                logging.info(
                    "  [%d/%d]  written=%d  failed=%d",
                    i + 1, len(py_files), n_written, n_failed,
                )

    logging.info("=" * 60)
    logging.info("DONE  written=%d  failed=%d", n_written, n_failed)
    logging.info("Output: %s", output_path)
    logging.info("=" * 60)


if __name__ == "__main__":
    main()
