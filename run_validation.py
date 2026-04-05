#!/usr/bin/env python3
"""
Zero-Shot Actor-Critic Validation — End-to-End CLI Entry Point.

Loads a YAML config, optionally overrides settings via CLI flags, and runs
the full ChartMimic benchmark with two passes:
  1. Baseline  — ChartCoder alone (no critic)
  2. Critic    — ChartCoder + iterative VL critic loop (Qwen3.5-122B)

Usage:
  # Quick smoke-test (5 samples)
  uv run python run_validation.py --config configs/default.yaml --num-samples 5

  # Full benchmark run
  uv run python run_validation.py --config configs/default.yaml

  # Skip baseline if already computed, re-run only critic with different config
  uv run python run_validation.py --config configs/default.yaml --skip-baseline

  # Override endpoints without editing the YAML
  uv run python run_validation.py \\
    --config configs/default.yaml \\
    --actor-url http://localhost:8080 \\
    --critic-url http://localhost:7001 \\
    --max-rounds 2 \\
    --num-samples 100 \\
    --output ./results/run_001
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Path setup — allow running from any working directory
# ---------------------------------------------------------------------------
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


# ---------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------
def _load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _apply_overrides(cfg: dict, args: argparse.Namespace) -> dict:
    """Apply CLI flag overrides on top of the YAML config."""
    if args.actor_url:
        cfg["actor"]["url"] = args.actor_url
    if args.actor_model_id:
        cfg["actor"]["model_id"] = args.actor_model_id
    if args.critic_url:
        cfg["critic"]["url"] = args.critic_url
    if args.critic_model_id:
        cfg["critic"]["model_id"] = args.critic_model_id
    if args.max_rounds is not None:
        cfg["loop"]["max_rounds"] = args.max_rounds
    if args.output:
        cfg["benchmark"]["output_dir"] = args.output
    if args.data:
        cfg["benchmark"]["dataset"] = args.data
    # num_samples is handled separately (passed to run())
    return cfg


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Zero-Shot Actor-Critic Validation on ChartMimic",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # Config file
    parser.add_argument("--config", default="configs/default.yaml",
                        help="Path to YAML config file")

    # Endpoint overrides (override config without editing YAML)
    parser.add_argument("--actor-url",       default=None,
                        help="Override actor.url in config")
    parser.add_argument("--actor-model-id",  default=None,
                        help="Override actor.model_id in config")
    parser.add_argument("--critic-url",      default=None,
                        help="Override critic.url in config")
    parser.add_argument("--critic-model-id", default=None,
                        help="Override critic.model_id in config")

    # Loop / benchmark overrides
    parser.add_argument("--max-rounds",  type=int,  default=None,
                        help="Override loop.max_rounds in config")
    parser.add_argument("--num-samples", type=int,  default=-1,
                        help="Number of samples to evaluate (-1 = all)")
    parser.add_argument("--data",        default=None,
                        help="Override benchmark.dataset path")
    parser.add_argument("--output",      default=None,
                        help="Override benchmark.output_dir path")

    # Run control
    parser.add_argument("--skip-baseline", action="store_true",
                        help="Skip baseline pass if results_baseline.jsonl already exists")
    parser.add_argument("--skip-critic", action="store_true",
                        help="Run baseline pass only; skip critic pass entirely")
    parser.add_argument("--seed", type=int, default=None,
                        help="Override benchmark.seed")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logging.getLogger("httpx").setLevel(logging.CRITICAL)

    # Load and patch config
    cfg = _load_config(args.config)
    cfg = _apply_overrides(cfg, args)
    if args.seed is not None:
        cfg["benchmark"]["seed"] = args.seed

    output_dir = Path(cfg["benchmark"]["output_dir"])

    logging.info("=" * 70)
    logging.info("Zero-Shot Actor-Critic Validation")
    logging.info("Config          : %s", args.config)
    logging.info("Actor           : %s  @ %s",
                 cfg["actor"]["model_id"], cfg["actor"]["url"])
    logging.info("Critic          : %s  @ %s",
                 cfg["critic"]["model_id"], cfg["critic"]["url"])
    logging.info("Max rounds      : %d", cfg["loop"]["max_rounds"])
    logging.info("Dataset         : %s", cfg["benchmark"]["dataset"])
    logging.info("Num samples     : %s",
                 args.num_samples if args.num_samples > 0 else "all")
    logging.info("Output dir      : %s", output_dir)
    logging.info("Skip baseline   : %s", args.skip_baseline)
    logging.info("=" * 70)

    # Run
    from eval.run_benchmark import run  # noqa: PLC0415
    run(
        cfg=cfg,
        output_dir=output_dir,
        num_samples=args.num_samples,
        skip_baseline=args.skip_baseline,
        skip_critic=args.skip_critic,
    )


if __name__ == "__main__":
    main()
