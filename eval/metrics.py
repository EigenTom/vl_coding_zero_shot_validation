"""
Evaluation metrics.

compute_ssim  — structural similarity between two PNG byte strings
execution_ok  — whether a code string renders without error
summary_stats — aggregate statistics over a list of per-sample result dicts
"""

from __future__ import annotations

import io
import logging
from typing import Any

import numpy as np
from PIL import Image


def compute_ssim(img_bytes_a: bytes, img_bytes_b: bytes) -> float:
    """
    Compute SSIM between two PNG byte strings.

    Both images are resized to the smaller of the two dimensions (using the
    ground-truth image size as the reference) before comparison.  Grayscale
    conversion is used so SSIM focuses on structural content rather than colour.

    Returns 0.0 on any failure.
    """
    try:
        from skimage.metrics import structural_similarity as ssim
    except ImportError:
        raise RuntimeError("scikit-image required: uv pip install scikit-image")

    try:
        img_a = Image.open(io.BytesIO(img_bytes_a)).convert("L")
        img_b = Image.open(io.BytesIO(img_bytes_b)).convert("L")

        # Resize img_a to img_b's size (img_b is assumed to be the GT)
        if img_a.size != img_b.size:
            img_a = img_a.resize(img_b.size, Image.LANCZOS)

        arr_a = np.array(img_a)
        arr_b = np.array(img_b)

        score, _ = ssim(arr_a, arr_b, full=True)
        return float(score)
    except Exception as exc:
        logging.debug("compute_ssim failed: %s", exc)
        return 0.0


def execution_ok(code: str, render_cfg: dict) -> bool:
    """
    Return True if the code string renders successfully (no exception, non-empty PNG).
    """
    from inference.render import render_chart_code  # local import to avoid circular dep
    return render_chart_code(code, render_cfg) is not None


def summary_stats(
    baseline: list[dict[str, Any]],
    critic:   list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Compute aggregate comparison statistics.

    Each list contains per-sample result dicts with keys:
      baseline_exec_ok  (bool)
      baseline_ssim     (float)
      critic_exec_ok    (bool)
      critic_ssim       (float)
      critic_rounds_used (int)
      critic_stopped_by  (str)

    Returns a dict suitable for formatted printing and JSON serialisation.
    """
    n = len(baseline)
    if n == 0:
        return {}

    # Execution rates
    b_exec = sum(1 for r in baseline if r["baseline_exec_ok"]) / n
    c_exec = sum(1 for r in critic   if r["critic_exec_ok"])   / n

    # SSIM — all samples (0.0 for failed renders)
    b_ssim_all = sum(r["baseline_ssim"] for r in baseline) / n
    c_ssim_all = sum(r["critic_ssim"]   for r in critic)   / n

    # SSIM — execution-only (only samples where BASELINE executed successfully)
    exec_pairs = [
        (b["baseline_ssim"], c["critic_ssim"])
        for b, c in zip(baseline, critic)
        if b["baseline_exec_ok"]
    ]
    n_exec = len(exec_pairs)
    b_ssim_exec = sum(p[0] for p in exec_pairs) / n_exec if n_exec else 0.0
    c_ssim_exec = sum(p[1] for p in exec_pairs) / n_exec if n_exec else 0.0

    # Critic-specific stats
    done_count  = sum(1 for r in critic if r.get("critic_stopped_by") == "done")
    avg_rounds  = sum(r.get("critic_rounds_used", 0) for r in critic) / n

    return {
        "n_samples":           n,
        "baseline_exec_rate":  b_exec,
        "critic_exec_rate":    c_exec,
        "delta_exec_rate":     c_exec - b_exec,
        "baseline_ssim_all":   b_ssim_all,
        "critic_ssim_all":     c_ssim_all,
        "delta_ssim_all":      c_ssim_all - b_ssim_all,
        "n_exec_samples":      n_exec,
        "baseline_ssim_exec":  b_ssim_exec,
        "critic_ssim_exec":    c_ssim_exec,
        "delta_ssim_exec":     c_ssim_exec - b_ssim_exec,
        "critic_done_rate":    done_count / n,
        "critic_avg_rounds":   avg_rounds,
    }


def format_summary_table(stats: dict[str, Any]) -> str:
    """Render summary stats as a human-readable table string."""
    n       = stats["n_samples"]
    n_exec  = stats["n_exec_samples"]

    lines = [
        "",
        f"ChartMimic Evaluation  (N={n}, exec_samples={n_exec})",
        "─" * 55,
        f"{'Metric':<30} {'Baseline':>9} {'+ Critic':>9} {'Δ':>7}",
        "─" * 55,
        _row("Execution Rate",
             stats["baseline_exec_rate"], stats["critic_exec_rate"],
             stats["delta_exec_rate"], pct=True),
        _row("SSIM (exec. samples only)",
             stats["baseline_ssim_exec"], stats["critic_ssim_exec"],
             stats["delta_ssim_exec"]),
        _row("SSIM (all samples)",
             stats["baseline_ssim_all"], stats["critic_ssim_all"],
             stats["delta_ssim_all"]),
        "─" * 55,
        f"{'Critic DONE rate':<30} {'—':>9} {stats['critic_done_rate']*100:>8.1f}%",
        f"{'Avg. critic rounds used':<30} {'—':>9} {stats['critic_avg_rounds']:>9.2f}",
        "─" * 55,
        "",
    ]
    return "\n".join(lines)


def _row(label: str, base: float, crit: float, delta: float, pct: bool = False) -> str:
    if pct:
        return (f"{label:<30} {base*100:>8.1f}%  {crit*100:>8.1f}%  "
                f"{delta*100:>+6.1f}%")
    return f"{label:<30} {base:>9.3f}  {crit:>9.3f}  {delta:>+7.3f}"
