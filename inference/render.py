"""
Chart code renderer — ChartMimic-compatible subprocess approach.

Mirrors /chart2code/utils/post_process/code_interpreter.py from ChartMimic:
  1. Strip any markdown fences from the code.
  2. Strip existing plt.savefig() and plt.show() calls.
  3. Append a standardised plt.savefig(output_path, bbox_inches="tight") call.
  4. Execute the script via subprocess with MPLBACKEND=Agg in the environment.
  5. Read and return the output PNG bytes.

Using subprocess (not exec()) avoids namespace pollution, matches the validated
rendering behaviour used by ChartMimic's own evaluation pipeline, and isolates
crashes from the main process.
"""

from __future__ import annotations

import logging
import os
import re
import subprocess
import tempfile
from pathlib import Path


def render_chart_code(code: str, cfg: dict) -> bytes | None:
    """
    Render a Python/Matplotlib code string to PNG bytes.

    Parameters
    ----------
    code : str
        Raw Python code, possibly wrapped in markdown fences.
    cfg : dict
        Rendering config section from the YAML config, expected keys:
          timeout_sec   (int)  subprocess timeout
          output_format (str)  "png" or "pdf"
          bbox_inches   (str)  passed to plt.savefig — typically "tight"

    Returns
    -------
    bytes | None
        PNG bytes on success; None if execution fails or times out.
    """
    timeout     = int(cfg.get("timeout_sec", 30))
    fmt         = cfg.get("output_format", "png")
    bbox_inches = cfg.get("bbox_inches", "tight")

    # ── 1. Strip markdown fences ─────────────────────────────────────────────
    # Remove ```python ... ``` or ``` ... ```
    code = re.sub(r"```(?:python)?\s*\n?([\s\S]*?)```", r"\1", code)

    # ── 2. Strip existing savefig / show calls ───────────────────────────────
    # Match multi-line calls (arguments may span lines) — simple greedy strip
    code = re.sub(r"plt\.savefig\s*\([^)]*\)\s*", "", code)
    code = re.sub(r"plt\.show\s*\([^)]*\)\s*",    "", code)
    # Also handle bare plt.show() with no args
    code = re.sub(r"plt\.show\s*\(\s*\)\s*", "", code)

    # ── 3. Build the rendering script ────────────────────────────────────────
    #    Create temp output file path first (we pass it into the script)
    out_fd, output_path = tempfile.mkstemp(suffix=f".{fmt}")
    os.close(out_fd)

    # We do NOT prepend "import matplotlib; matplotlib.use('Agg')" because
    # MPLBACKEND=Agg is set in the subprocess environment — this is cleaner
    # and avoids conflicts if the code imports matplotlib at the top.
    script = (
        f"{code}\n\n"
        f"# --- appended by render.py ---\n"
        f"import matplotlib.pyplot as _plt_render\n"
        f"_plt_render.savefig({output_path!r}, bbox_inches={bbox_inches!r})\n"
    )

    script_fd, script_path = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(script_fd, "w", encoding="utf-8") as f:
            f.write(script)

        # ── 4. Execute via subprocess ─────────────────────────────────────────
        env = os.environ.copy()
        env["MPLBACKEND"] = "Agg"   # non-interactive backend, no display needed

        result = subprocess.run(
            ["python3", script_path],
            timeout=timeout,
            capture_output=True,
            text=True,
            env=env,
        )

        if result.returncode != 0:
            stderr_snippet = (result.stderr or "")[:300].strip()
            logging.debug("Render subprocess failed (rc=%d): %s", result.returncode, stderr_snippet)
            return None

        # ── 5. Read output image ──────────────────────────────────────────────
        out = Path(output_path)
        if not out.exists() or out.stat().st_size == 0:
            logging.debug("Render subprocess exited 0 but output file is empty/missing")
            return None

        return out.read_bytes()

    except subprocess.TimeoutExpired:
        logging.debug("Render subprocess timed out after %ds", timeout)
        return None
    except Exception as exc:
        logging.debug("Render error: %s", exc)
        return None
    finally:
        # Clean up temp files
        for p in [script_path, output_path]:
            try:
                os.unlink(p)
            except OSError:
                pass
