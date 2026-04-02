"""
Actor-Critic Inference Loop.

Algorithm
---------
Round 0 (Actor — initial generation):
    code_0 = actor.generate(target_image)
    img_0  = render(code_0)
    → if render fails: stop with stopped_by="render_fail_round0"

Round k (k = 1 … max_rounds):
    feedback = critic.evaluate(img_{k-1}, target_image)
    → if feedback == "DONE": stop with stopped_by="done"
    → if critic API fails: stop with stopped_by="critic_fail"

    code_k = actor.refine(target_image, code_{k-1}, feedback)
    → if actor API fails: stop with stopped_by="actor_fail"

    img_k  = render(code_k)
    → if render fails: stop with stopped_by="render_fail"
      (keep code_{k-1} as final_code)

After max_rounds: stop with stopped_by="max_rounds"

Design notes
------------
- The critic sees ONLY images — no code.  It outputs plain natural language
  (or "DONE").  This is a pure visual evaluation role.
- The actor does ALL code work: initial generation and all refinements.
- Each round's data is recorded in per_round for later analysis.
"""

from __future__ import annotations

import base64
import logging
import time
from dataclasses import dataclass, field
from typing import Any

from inference import actor_client, critic_client
from inference.render import render_chart_code


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class RoundRecord:
    round: int                    # 0 = actor initial; 1..N = critic-actor rounds
    code: str                     # code produced at the end of this round
    render_ok: bool               # whether the code rendered successfully
    rendered_image_b64: str       # base64 PNG bytes; empty string if render_ok=False
    critic_feedback: str = ""     # "" for round 0; critic response for rounds >= 1
                                  # "DONE" means critic approved the PREVIOUS round's output


@dataclass
class LoopResult:
    example_id: str
    final_code: str               # best code to evaluate (last successfully rendered)
    stopped_by: str               # "done" | "max_rounds" | "render_fail_round0" |
                                  # "render_fail" | "critic_fail" | "actor_fail"
    rounds_used: int              # number of critic-actor rounds executed (0 = baseline only)
    per_round: list[RoundRecord] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def run_loop(sample: dict[str, Any], cfg: dict) -> LoopResult:
    """
    Run the full actor-critic loop for one benchmark sample.

    Parameters
    ----------
    sample : dict
        A single ChartMimic JSONL record with keys:
          example_id      (str)
          input_image_b64 (str)  base64 PNG — sent to actor
          gt_code         (str)  ground truth code (not used here)
          gt_image_b64    (str)  ground truth render (not used here)
    cfg : dict
        Full parsed YAML config.

    Returns
    -------
    LoopResult
    """
    example_id       = sample["example_id"]
    target_image_b64 = sample["input_image_b64"]   # the chart image actor must reproduce
    max_rounds       = int(cfg["loop"]["max_rounds"])
    render_cfg       = cfg["rendering"]
    records: list[RoundRecord] = []

    # ── Round 0: Actor initial generation ────────────────────────────────────
    t0 = time.time()
    code_0 = actor_client.generate(target_image_b64, cfg)
    logging.info("[Loop][%s] round=0  actor api=%.1fs", example_id, time.time() - t0)

    if not code_0:
        logging.warning("[Loop][%s] round=0 actor returned None", example_id)
        return LoopResult(
            example_id=example_id,
            final_code="",
            stopped_by="actor_fail",
            rounds_used=0,
            per_round=[RoundRecord(round=0, code="", render_ok=False,
                                   rendered_image_b64="")],
        )

    t1 = time.time()
    img_0 = render_chart_code(code_0, render_cfg)
    logging.info("[Loop][%s] round=0  render=%s  %.1fs",
                 example_id, "ok" if img_0 else "FAIL", time.time() - t1)

    records.append(RoundRecord(
        round=0,
        code=code_0,
        render_ok=img_0 is not None,
        rendered_image_b64=base64.b64encode(img_0).decode() if img_0 else "",
    ))

    if img_0 is None:
        return LoopResult(
            example_id=example_id,
            final_code=code_0,
            stopped_by="render_fail_round0",
            rounds_used=0,
            per_round=records,
        )

    current_code  = code_0
    current_img   = img_0

    # ── Rounds 1..max_rounds: Critic evaluation → Actor refinement ───────────
    for rnd in range(1, max_rounds + 1):

        # Critic call
        current_b64 = base64.b64encode(current_img).decode()
        t2 = time.time()
        feedback = critic_client.evaluate(current_b64, target_image_b64, cfg)
        logging.info("[Loop][%s] round=%d  critic api=%.1fs  feedback=%r",
                     example_id, rnd, time.time() - t2,
                     (feedback or "")[:80])

        if feedback is None:
            logging.warning("[Loop][%s] round=%d critic returned None", example_id, rnd)
            # Tag the previous record with the failed critic call
            records[-1].critic_feedback = "CRITIC_API_FAIL"
            return LoopResult(
                example_id=example_id,
                final_code=current_code,
                stopped_by="critic_fail",
                rounds_used=rnd - 1,
                per_round=records,
            )

        # Mark critic feedback on the PREVIOUS round's record
        records[-1].critic_feedback = feedback

        if feedback.strip().upper() == "DONE":
            logging.info("[Loop][%s] round=%d  critic=DONE", example_id, rnd)
            return LoopResult(
                example_id=example_id,
                final_code=current_code,
                stopped_by="done",
                rounds_used=rnd - 1,
                per_round=records,
            )

        # Actor refinement
        t3 = time.time()
        new_code = actor_client.refine(target_image_b64, current_code, feedback, cfg)
        logging.info("[Loop][%s] round=%d  actor refine api=%.1fs",
                     example_id, rnd, time.time() - t3)

        if not new_code:
            logging.warning("[Loop][%s] round=%d actor refine returned None", example_id, rnd)
            return LoopResult(
                example_id=example_id,
                final_code=current_code,
                stopped_by="actor_fail",
                rounds_used=rnd - 1,
                per_round=records,
            )

        t4 = time.time()
        new_img = render_chart_code(new_code, render_cfg)
        logging.info("[Loop][%s] round=%d  render=%s  %.1fs",
                     example_id, rnd, "ok" if new_img else "FAIL", time.time() - t4)

        if new_img is None:
            # Refinement broke rendering — keep previous good code
            records.append(RoundRecord(
                round=rnd,
                code=new_code,
                render_ok=False,
                rendered_image_b64="",
            ))
            return LoopResult(
                example_id=example_id,
                final_code=current_code,
                stopped_by="render_fail",
                rounds_used=rnd,
                per_round=records,
            )

        records.append(RoundRecord(
            round=rnd,
            code=new_code,
            render_ok=True,
            rendered_image_b64=base64.b64encode(new_img).decode(),
        ))
        current_code = new_code
        current_img  = new_img

    # Max rounds reached
    return LoopResult(
        example_id=example_id,
        final_code=current_code,
        stopped_by="max_rounds",
        rounds_used=max_rounds,
        per_round=records,
    )
