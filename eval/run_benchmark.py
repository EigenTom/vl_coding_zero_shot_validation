"""
ChartMimic Benchmark Runner.

Runs two evaluation passes over the ChartMimic test set:

  Pass 1 — Baseline:
    ChartCoder generates code once (round 0 only); no critic involvement.

  Pass 2 — Critic-assisted:
    Full actor-critic loop (run_loop) for each sample; uses the final code.

Both passes evaluate the resulting code using ChartMimic's official semantic
metrics (TextEvaluator, ChartTypeEvaluator, ColorEvaluator, LayoutEvaluator).
Execution success is determined via render_chart_code (subprocess + Agg).

Results are written to JSONL files in the output directory, and a summary
table is printed to stdout and saved as summary.txt.

Optionally, Pass 1 can be skipped if baseline results already exist
(--skip-baseline flag) to save API cost when re-running with a different config.

Dataset JSONL format (from setup/download_chartmimic.py):
  {
    "example_id":      "bar_3",
    "gt_code":         "...",
    "gt_py_path":      "/abs/path/to/bar_3.py",
    "input_image_b64": "<base64 PNG>"
  }
"""

from __future__ import annotations

import argparse
import json
import logging
import random
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

# Make sure the project root is on sys.path when this module is run directly
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from inference import actor_client
from inference.actor_critic_loop import run_loop
from inference.render import render_chart_code
from eval.metrics import compute_semantic_metrics, summary_stats, format_summary_table


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _load_dataset(path: str, num_samples: int, seed: int) -> list[dict[str, Any]]:
    samples = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))
    if num_samples > 0:
        rng = random.Random(seed)
        samples = rng.sample(samples, min(num_samples, len(samples)))
    logging.info("Loaded %d samples from %s", len(samples), path)
    return samples


def _evaluate_code(code: str, sample: dict, render_cfg: dict) -> dict:
    """
    Render code and run ChartMimic semantic evaluation.

    Returns a dict with keys:
      exec_ok, text_f1, chart_type_f1, color_f1, layout_f1
    """
    # Render check (fast; also produces the image for critic comparison)
    png = render_chart_code(code, render_cfg)
    exec_ok = png is not None

    # Semantic metrics (slower; requires ChartMimic evaluator subprocess)
    gt_py_path = sample.get("gt_py_path", "")
    if exec_ok and gt_py_path:
        sem = compute_semantic_metrics(code, gt_py_path)
        # Overwrite exec_ok from the semantic evaluator if render succeeded but
        # evaluator says exec failed (e.g. the code runs but produces nothing useful)
        # Keep render-based exec_ok as the primary signal.
    else:
        from eval.chartmimic_evaluator import _empty_metrics
        sem = _empty_metrics()
        sem["exec_ok"] = exec_ok

    return {
        "exec_ok":       exec_ok,
        "text_f1":       sem.get("text_f1",       0.0),
        "chart_type_f1": sem.get("chart_type_f1", 0.0),
        "color_f1":      sem.get("color_f1",      0.0),
        "layout_f1":     sem.get("layout_f1",     0.0),
    }


# ---------------------------------------------------------------------------
# Baseline pass
# ---------------------------------------------------------------------------
def run_baseline_pass(
    samples: list[dict[str, Any]],
    cfg: dict,
    output_path: Path,
) -> list[dict[str, Any]]:
    """Generate code with ChartCoder (no critic) and evaluate."""
    render_cfg = cfg["rendering"]
    results: list[dict[str, Any]] = []

    logging.info("=" * 60)
    logging.info("BASELINE PASS  (%d samples)", len(samples))
    logging.info("=" * 60)

    try:
        from tqdm import tqdm
        iterator = tqdm(samples, desc="Baseline", unit="sample")
    except ImportError:
        iterator = samples

    for sample in iterator:
        eid = sample["example_id"]
        t0  = time.time()

        code = actor_client.generate(sample["input_image_b64"], cfg)
        if not code:
            logging.warning("[Baseline][%s] actor returned None", eid)
            results.append({
                "example_id":            eid,
                "baseline_exec_ok":      False,
                "baseline_text_f1":      0.0,
                "baseline_chart_type_f1": 0.0,
                "baseline_color_f1":     0.0,
                "baseline_layout_f1":    0.0,
                "baseline_code":         "",
            })
            continue

        ev = _evaluate_code(code, sample, render_cfg)

        logging.info(
            "[Baseline][%s]  exec=%s  text_f1=%.3f  color_f1=%.3f  %.1fs",
            eid, ev["exec_ok"], ev["text_f1"], ev["color_f1"], time.time() - t0,
        )
        results.append({
            "example_id":              eid,
            "baseline_exec_ok":        ev["exec_ok"],
            "baseline_text_f1":        ev["text_f1"],
            "baseline_chart_type_f1":  ev["chart_type_f1"],
            "baseline_color_f1":       ev["color_f1"],
            "baseline_layout_f1":      ev["layout_f1"],
            "baseline_code":           code,
        })

    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            json.dump(r, f, ensure_ascii=False)
            f.write("\n")
    logging.info("Baseline results saved → %s", output_path)
    return results


# ---------------------------------------------------------------------------
# Critic-assisted pass
# ---------------------------------------------------------------------------
def run_critic_pass(
    samples: list[dict[str, Any]],
    cfg: dict,
    output_path: Path,
) -> list[dict[str, Any]]:
    """Run full actor-critic loop and evaluate final code."""
    render_cfg = cfg["rendering"]
    results: list[dict[str, Any]] = []

    logging.info("=" * 60)
    logging.info("CRITIC PASS  (%d samples, max_rounds=%d)",
                 len(samples), cfg["loop"]["max_rounds"])
    logging.info("=" * 60)

    try:
        from tqdm import tqdm
        iterator = tqdm(samples, desc="Critic", unit="sample")
    except ImportError:
        iterator = samples

    for sample in iterator:
        eid = sample["example_id"]
        t0  = time.time()

        loop_res = run_loop(sample, cfg)
        final_code = loop_res.final_code or ""

        ev = _evaluate_code(final_code, sample, render_cfg) if final_code else {
            "exec_ok": False, "text_f1": 0.0, "chart_type_f1": 0.0,
            "color_f1": 0.0, "layout_f1": 0.0,
        }

        logging.info(
            "[Critic][%s]  stopped=%s  rounds=%d  exec=%s  text_f1=%.3f  %.1fs",
            eid, loop_res.stopped_by, loop_res.rounds_used,
            ev["exec_ok"], ev["text_f1"], time.time() - t0,
        )

        results.append({
            "example_id":             eid,
            "critic_exec_ok":         ev["exec_ok"],
            "critic_text_f1":         ev["text_f1"],
            "critic_chart_type_f1":   ev["chart_type_f1"],
            "critic_color_f1":        ev["color_f1"],
            "critic_layout_f1":       ev["layout_f1"],
            "critic_final_code":      final_code,
            "critic_rounds_used":     loop_res.rounds_used,
            "critic_stopped_by":      loop_res.stopped_by,
            "per_round": [asdict(r) for r in loop_res.per_round],
        })

    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            json.dump(r, f, ensure_ascii=False)
            f.write("\n")
    logging.info("Critic results saved → %s", output_path)
    return results


# ---------------------------------------------------------------------------
# Main entry point (when called as a module)
# ---------------------------------------------------------------------------
def run(
    cfg: dict,
    output_dir: Path,
    num_samples: int = -1,
    skip_baseline: bool = False,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    bench_cfg = cfg["benchmark"]
    data_path = bench_cfg["dataset"]
    seed      = int(bench_cfg.get("seed", 42))
    n         = num_samples if num_samples >= 0 else int(bench_cfg.get("num_samples", -1))

    samples = _load_dataset(data_path, n, seed)

    baseline_path = output_dir / "results_baseline.jsonl"
    critic_path   = output_dir / "results_critic.jsonl"
    summary_path  = output_dir / "summary.txt"

    # ── Baseline ──────────────────────────────────────────────────────────────
    if skip_baseline and baseline_path.exists():
        logging.info("Skipping baseline pass (--skip-baseline set, file exists)")
        baseline_results = []
        with open(baseline_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    baseline_results.append(json.loads(line))
    else:
        baseline_results = run_baseline_pass(samples, cfg, baseline_path)

    # ── Critic ────────────────────────────────────────────────────────────────
    critic_results = run_critic_pass(samples, cfg, critic_path)

    # Align by example_id
    base_map   = {r["example_id"]: r for r in baseline_results}
    critic_map = {r["example_id"]: r for r in critic_results}
    common_ids = [
        s["example_id"] for s in samples
        if s["example_id"] in base_map and s["example_id"] in critic_map
    ]

    if not common_ids:
        logging.warning("No overlapping example_ids between baseline and critic results.")
        return

    aligned_base   = [base_map[eid]   for eid in common_ids]
    aligned_critic = [critic_map[eid] for eid in common_ids]

    # Merge baseline fields into critic records for the combined JSONL
    for b, c in zip(aligned_base, aligned_critic):
        c.update({k: v for k, v in b.items() if k not in c})

    combined_path = output_dir / "results_combined.jsonl"
    with open(combined_path, "w", encoding="utf-8") as f:
        for r in aligned_critic:
            json.dump(r, f, ensure_ascii=False)
            f.write("\n")
    logging.info("Combined results saved → %s", combined_path)

    # ── Summary ───────────────────────────────────────────────────────────────
    stats = summary_stats(aligned_base, aligned_critic)
    table = format_summary_table(stats)
    print(table)
    summary_path.write_text(table, encoding="utf-8")
    logging.info("Summary saved → %s", summary_path)
