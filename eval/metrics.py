"""
Evaluation metrics for the ChartMimic zero-shot actor-critic validation.

compute_semantic_metrics  — run ChartMimic's official semantic evaluators
compute_ssim              — fast pixel-level SSIM (kept as a utility)
summary_stats             — aggregate statistics over per-sample result dicts
format_summary_table      — render stats as a human-readable ASCII table
"""

from __future__ import annotations

import io
import logging
from typing import Any

import numpy as np
from PIL import Image


# ---------------------------------------------------------------------------
# Primary metric: ChartMimic semantic evaluation
# ---------------------------------------------------------------------------

def compute_semantic_metrics(generated_code: str, gt_py_path: str) -> dict:
    """
    Run ChartMimic's official semantic evaluators on one generated code sample.

    Delegates to eval.chartmimic_evaluator, which spawns a subprocess with the
    correct working directory and environment for the ChartMimic evaluation code.

    Parameters
    ----------
    generated_code : str
        Python/Matplotlib code produced by the actor (may include md fences).
    gt_py_path : str
        Absolute path to the GT .py file from the ChartMimic dataset.

    Returns
    -------
    dict
        Keys: exec_ok (bool), text_f1, chart_type_f1, color_f1, layout_f1 (float).
    """
    from eval.chartmimic_evaluator import evaluate  # local import — avoids side-effects
    return evaluate(generated_code, gt_py_path)


# ---------------------------------------------------------------------------
# Secondary metric: SSIM (pixel-level, fast, kept as an optional utility)
# ---------------------------------------------------------------------------

def compute_ssim(img_bytes_a: bytes, img_bytes_b: bytes) -> float:
    """
    Compute SSIM between two PNG byte strings.

    Both images are resized to the ground-truth image size before comparison.
    Returns 0.0 on any failure.
    """
    try:
        from skimage.metrics import structural_similarity as ssim
    except ImportError:
        raise RuntimeError("scikit-image required: uv pip install scikit-image")

    try:
        img_a = Image.open(io.BytesIO(img_bytes_a)).convert("L")
        img_b = Image.open(io.BytesIO(img_bytes_b)).convert("L")

        if img_a.size != img_b.size:
            img_a = img_a.resize(img_b.size, Image.LANCZOS)

        arr_a = np.array(img_a)
        arr_b = np.array(img_b)

        score, _ = ssim(arr_a, arr_b, full=True)
        return float(score)
    except Exception as exc:
        logging.debug("compute_ssim failed: %s", exc)
        return 0.0


# ---------------------------------------------------------------------------
# Aggregate statistics
# ---------------------------------------------------------------------------

def summary_stats(
    baseline: list[dict[str, Any]],
    critic:   list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Compute aggregate comparison statistics over baseline and critic passes.

    Each list contains per-sample result dicts produced by run_benchmark.py.

    Baseline keys expected:
      baseline_exec_ok  (bool)
      baseline_text_f1, baseline_chart_type_f1, baseline_color_f1, baseline_layout_f1  (float)

    Critic keys expected:
      critic_exec_ok  (bool)
      critic_text_f1, critic_chart_type_f1, critic_color_f1, critic_layout_f1  (float)
      critic_rounds_used  (int)
      critic_stopped_by   (str)
    """
    n = len(baseline)
    if n == 0:
        return {}

    def _mean(records: list[dict], key: str) -> float:
        return sum(r.get(key, 0.0) for r in records) / n

    def _rate(records: list[dict], key: str) -> float:
        return sum(1 for r in records if r.get(key)) / n

    # Execution rates
    b_exec = _rate(baseline, "baseline_exec_ok")
    c_exec = _rate(critic,   "critic_exec_ok")

    # Semantic metrics — all samples (0.0 for failed renders)
    metrics = ["text_f1", "chart_type_f1", "color_f1", "layout_f1"]
    b_scores = {m: _mean(baseline, f"baseline_{m}") for m in metrics}
    c_scores = {m: _mean(critic,   f"critic_{m}")   for m in metrics}

    # Semantic metrics — exec-only (only samples where BASELINE executed)
    exec_baseline = [b for b in baseline if b.get("baseline_exec_ok")]
    exec_critic   = [
        c for b, c in zip(baseline, critic) if b.get("baseline_exec_ok")
    ]
    n_exec = len(exec_baseline)

    def _mean_exec(records: list[dict], key: str) -> float:
        if not records:
            return 0.0
        return sum(r.get(key, 0.0) for r in records) / len(records)

    b_scores_exec = {m: _mean_exec(exec_baseline, f"baseline_{m}") for m in metrics}
    c_scores_exec = {m: _mean_exec(exec_critic,   f"critic_{m}")   for m in metrics}

    # Critic-specific stats
    done_count = sum(1 for r in critic if r.get("critic_stopped_by") == "done")
    avg_rounds = sum(r.get("critic_rounds_used", 0) for r in critic) / n

    return {
        "n_samples":              n,
        "n_exec_samples":         n_exec,
        # Execution
        "baseline_exec_rate":     b_exec,
        "critic_exec_rate":       c_exec,
        "delta_exec_rate":        c_exec - b_exec,
        # Text F1
        "baseline_text_f1":       b_scores["text_f1"],
        "critic_text_f1":         c_scores["text_f1"],
        "delta_text_f1":          c_scores["text_f1"] - b_scores["text_f1"],
        # Chart-type F1
        "baseline_chart_type_f1": b_scores["chart_type_f1"],
        "critic_chart_type_f1":   c_scores["chart_type_f1"],
        "delta_chart_type_f1":    c_scores["chart_type_f1"] - b_scores["chart_type_f1"],
        # Color F1
        "baseline_color_f1":      b_scores["color_f1"],
        "critic_color_f1":        c_scores["color_f1"],
        "delta_color_f1":         c_scores["color_f1"] - b_scores["color_f1"],
        # Layout F1
        "baseline_layout_f1":     b_scores["layout_f1"],
        "critic_layout_f1":       c_scores["layout_f1"],
        "delta_layout_f1":        c_scores["layout_f1"] - b_scores["layout_f1"],
        # Exec-only semantic metrics (with per-metric deltas)
        "baseline_text_f1_exec":       b_scores_exec["text_f1"],
        "critic_text_f1_exec":         c_scores_exec["text_f1"],
        "delta_text_f1_exec":          c_scores_exec["text_f1"] - b_scores_exec["text_f1"],
        "baseline_chart_type_f1_exec": b_scores_exec["chart_type_f1"],
        "critic_chart_type_f1_exec":   c_scores_exec["chart_type_f1"],
        "delta_chart_type_f1_exec":    c_scores_exec["chart_type_f1"] - b_scores_exec["chart_type_f1"],
        "baseline_color_f1_exec":      b_scores_exec["color_f1"],
        "critic_color_f1_exec":        c_scores_exec["color_f1"],
        "delta_color_f1_exec":         c_scores_exec["color_f1"] - b_scores_exec["color_f1"],
        "baseline_layout_f1_exec":     b_scores_exec["layout_f1"],
        "critic_layout_f1_exec":       c_scores_exec["layout_f1"],
        "delta_layout_f1_exec":        c_scores_exec["layout_f1"] - b_scores_exec["layout_f1"],
        # Critic loop stats
        "critic_done_rate":       done_count / n,
        "critic_avg_rounds":      avg_rounds,
    }


# ---------------------------------------------------------------------------
# Summary table formatter
# ---------------------------------------------------------------------------

def format_summary_table(stats: dict[str, Any]) -> str:
    """Render summary stats as a human-readable ASCII table."""
    n      = stats["n_samples"]
    n_exec = stats["n_exec_samples"]

    def row(label: str, b_key: str, c_key: str, d_key: str, pct: bool = False) -> str:
        b = stats[b_key]
        c = stats[c_key]
        d = stats[d_key]
        if pct:
            return f"{label:<32} {b*100:>8.1f}%  {c*100:>8.1f}%  {d*100:>+7.1f}%"
        return f"{label:<32} {b:>9.3f}  {c:>9.3f}  {d:>+8.3f}"

    sep = "─" * 62

    lines = [
        "",
        f"ChartMimic Semantic Evaluation  (N={n}, exec_samples={n_exec})",
        sep,
        f"{'Metric':<32} {'Baseline':>9}  {'+ Critic':>9}  {'Δ':>8}",
        sep,
        "── All samples ─────────────────────────────────────────────",
        row("Execution Rate",      "baseline_exec_rate",     "critic_exec_rate",     "delta_exec_rate",     pct=True),
        row("Text F1",             "baseline_text_f1",       "critic_text_f1",       "delta_text_f1"),
        row("Chart-Type F1",       "baseline_chart_type_f1", "critic_chart_type_f1", "delta_chart_type_f1"),
        row("Color F1",            "baseline_color_f1",      "critic_color_f1",      "delta_color_f1"),
        row("Layout F1",           "baseline_layout_f1",     "critic_layout_f1",     "delta_layout_f1"),
        "── Exec-only samples ───────────────────────────────────────",
        row("Text F1 (exec)",      "baseline_text_f1_exec",       "critic_text_f1_exec",       "delta_text_f1_exec")       if "baseline_text_f1_exec"       in stats else "",
        row("Chart-Type F1 (exec)","baseline_chart_type_f1_exec","critic_chart_type_f1_exec",  "delta_chart_type_f1_exec") if "baseline_chart_type_f1_exec" in stats else "",
        row("Color F1 (exec)",     "baseline_color_f1_exec",     "critic_color_f1_exec",       "delta_color_f1_exec")      if "baseline_color_f1_exec"      in stats else "",
        row("Layout F1 (exec)",    "baseline_layout_f1_exec",    "critic_layout_f1_exec",      "delta_layout_f1_exec")     if "baseline_layout_f1_exec"     in stats else "",
        sep,
        f"{'Critic DONE rate':<32} {'—':>9}  {stats['critic_done_rate']*100:>8.1f}%",
        f"{'Avg critic rounds used':<32} {'—':>9}  {stats['critic_avg_rounds']:>9.2f}",
        sep,
        "",
    ]
    # Remove any empty strings (missing exec-only rows)
    return "\n".join(ln for ln in lines if ln != "")
