# Task: Zero-Shot Actor-Critic Validation for VL Chart-to-Code

## Background & Motivation

We are developing a training pipeline (`vincicoder_repurpose/`) to synthesise training data for a standalone **VL Critic model**. Before investing in full training, we want to **validate the core hypothesis** with a zero-shot experiment:

> **Hypothesis**: Prompting a powerful VLM (Qwen3.5-122B-A10B) to act as a visual critic — comparing rendered output against the target chart and providing natural-language feedback — enables a specialist chart-to-code model (ChartCoder) to iteratively improve its output.

**Test subject**: [ChartCoder](https://github.com/thunlp/ChartCoder) (`xxxllz/ChartCoder`, 7B) acts as the **actor**: a specialist chart image-to-code model with a fixed public benchmark (ChartMimic) and known baseline numbers.

**Setup**: ChartCoder generates initial code → iterative VL critic loop (Qwen3.5-122B via vLLM) provides visual feedback → ChartCoder refines code → evaluation on ChartMimic benchmark.

If execution rate / visual similarity improves measurably over ChartCoder baseline, the critic concept is validated and we proceed to full training.

---

## Revised Design Decisions (from initial plan)

### 1. True Actor-Critic Separation

The critic does **not** generate code. It only compares two images and writes natural-language feedback. The actor (ChartCoder) does all code generation.

- **Critic** sees: `[IMAGE 1]` current rendering + `[IMAGE 2]` target chart
  - Output A: the single word `DONE` (charts match)
  - Output B: natural-language description of visual differences (no tags, no code)
- **Actor** receives: target image + previous code + critic's feedback text → generates improved code

This is a clean separation: critic = pure visual evaluator, actor = code generator. It also more faithfully mimics the intended critic model role.

### 2. Rendering Uses ChartMimic's Validated Approach

ChartMimic's evaluation pipeline (`/chart2code/utils/post_process/code_interpreter.py`) renders code by:
1. Extracting code from any markdown fences
2. Stripping existing `plt.savefig()` and `plt.show()` calls
3. Appending: `plt.savefig("{output_path}", bbox_inches="tight")`
4. Executing via **subprocess** (`python3 temp_script.py`)

We adopt this approach exactly. This ensures rendering behaviour matches the benchmark's own evaluation, avoids the unknown deficiencies of the `matplotlib Agg + exec()` approach used in `vincicoder_repurpose`, and produces output compatible with ChartMimic's evaluation tools.

### 3. Prompts, Inference Params, and Endpoints in a YAML Config

All prompts (as multi-line strings), model inference parameters, API endpoints, loop parameters, and benchmark settings live in `configs/default.yaml`. Code only reads from this config — no hardcoded strings or values in Python files.

---

## Codebase Location

All code lives in `/data/yilu/zero_shot_validation/`.

---

## File Structure

```
zero_shot_validation/
│
├── task.md                          # This document
├── requirements.txt                 # Python dependencies for this project
│
├── configs/
│   └── default.yaml                 # ALL prompts, inference params, endpoints, benchmark settings
│
├── setup/
│   ├── download_chartmimic.py       # Download ChartMimic benchmark from HuggingFace
│   └── download_chartcoder.py       # Download ChartCoder model weights from HuggingFace
│
├── serve/
│   └── serve_chartcoder.py          # FastAPI server: wraps ChartCoder as OpenAI-compatible API
│
├── inference/
│   ├── render.py                    # Subprocess-based chart rendering (ChartMimic-compatible)
│   ├── actor_client.py              # HTTP client: calls actor model via OpenAI-compatible API
│   ├── critic_client.py             # HTTP client: calls critic model via OpenAI-compatible API
│   └── actor_critic_loop.py         # Core loop: actor generates, critic evaluates, actor refines
│
├── eval/
│   ├── metrics.py                   # SSIM, execution rate, improvement delta
│   └── run_benchmark.py             # ChartMimic benchmark runner (baseline + critic loop)
│
└── run_validation.py                # End-to-end CLI entry point
```

---

## `configs/default.yaml`

```yaml
# ─────────────────────────────────────────────────────────────────────────────
# API Endpoints
# ─────────────────────────────────────────────────────────────────────────────
actor:
  url: "http://localhost:8080"
  model_id: "ChartCoder"

critic:
  url: "http://localhost:7001"
  model_id: "Qwen/Qwen3.5-122B-A10B"

# ─────────────────────────────────────────────────────────────────────────────
# Inference Parameters
# ─────────────────────────────────────────────────────────────────────────────
actor_params:
  temperature: 0.1
  top_p: 0.95
  max_tokens: 2048

critic_params:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  min_p: 0.0
  presence_penalty: 0.0
  repetition_penalty: 1.0
  max_tokens: 1024   # feedback only, no code — short output

# ─────────────────────────────────────────────────────────────────────────────
# Prompts
# ─────────────────────────────────────────────────────────────────────────────
prompts:
  # Actor: initial code generation from chart image
  actor_initial: |
    Convert this chart image to Python/Matplotlib code that reproduces it as accurately
    as possible. Output only the complete Python code with no explanations or markdown fences.

  # Actor: refinement given previous code + critic feedback
  # Placeholders: {previous_code}, {critic_feedback}
  actor_refine: |
    Here is the Python/Matplotlib code that was previously generated to reproduce the target chart:

    ```python
    {previous_code}
    ```

    A visual review of the rendered output identified the following differences from the target:

    {critic_feedback}

    Please fix the code to address all the listed issues. Output only the complete corrected
    Python code with no explanations or markdown fences.

  # Critic: system prompt (image-only evaluation, no code)
  critic_system: |
    You are a visual chart critic. Your sole task is to compare two chart images.

    If the charts are visually equivalent or very close, respond with exactly one word: DONE

    Otherwise, describe all visual differences clearly and specifically so a programmer
    can fix the code. Be precise: name chart elements, values, colors, labels, and positions.
    Do not suggest code changes — only describe what is visually wrong.

  # Critic: user prompt
  # [IMAGE 1] and [IMAGE 2] are injected as base64 images by the client
  critic_user: |
    [IMAGE 1] = Current rendering of the generated code
    [IMAGE 2] = Target chart to reproduce

    Compare both images carefully. Identify all visual discrepancies including:
    - Chart type and overall structure
    - Colors, line styles, and markers
    - Axis labels, tick values, and scales
    - Title, legend text, and position
    - Missing or extra elements
    - Data values and proportions

    If the charts match closely: output exactly DONE
    Otherwise: list all differences in plain language. Be specific and actionable.

# ─────────────────────────────────────────────────────────────────────────────
# Loop Parameters
# ─────────────────────────────────────────────────────────────────────────────
loop:
  max_rounds: 5          # maximum critic-actor refinement rounds (not counting round 0)

# ─────────────────────────────────────────────────────────────────────────────
# Rendering Parameters (ChartMimic-compatible)
# ─────────────────────────────────────────────────────────────────────────────
rendering:
  timeout_sec: 30        # subprocess timeout per render attempt
  output_format: "png"   # savefig format appended to stripped code
  bbox_inches: "tight"   # matches ChartMimic evaluation

# ─────────────────────────────────────────────────────────────────────────────
# Benchmark Settings
# ─────────────────────────────────────────────────────────────────────────────
benchmark:
  dataset: "./data/chartmimic/test.jsonl"
  num_samples: -1        # -1 = all 600 samples
  output_dir: "./results"
  seed: 42
```

---

## Component Design

### `setup/download_chartmimic.py`

Downloads ChartMimic from `ChartMimic/ChartMimic` on HuggingFace.

- Filters to `Task == "image-to-code"` split
- Saves to `./data/chartmimic/test.jsonl` — one JSON object per line:
  ```json
  {
    "example_id": "...",
    "input_image_b64": "...",
    "gt_code": "...",
    "gt_image_b64": "..."
  }
  ```
- Fields used: `ExampleID`, `InputFigurePreview` (input chart image), `GroundTruthFigureCode`, `GroundTruthFigurePreview`
- **CLI**: `uv run python setup/download_chartmimic.py [--output ./data/chartmimic]`

### `setup/download_chartcoder.py`

Downloads ChartCoder weights from `xxxllz/ChartCoder`.

- Uses `snapshot_download(repo_id="xxxllz/ChartCoder", local_dir="./models/ChartCoder", local_dir_use_symlinks=False)`
- Supports `HF_ENDPOINT` env var for mirror fallback
- **CLI**: `uv run python setup/download_chartcoder.py [--output ./models/ChartCoder]`

---

### `serve/serve_chartcoder.py`

ChartCoder uses a custom LLaVA architecture (`deepseek-coder-6.7b-instruct` + SigLIP), which is **not natively vLLM-compatible**. This FastAPI server wraps it behind an OpenAI Chat Completions-compatible endpoint.

**Endpoint**: `POST /v1/chat/completions`

**Request**: standard OpenAI multimodal format — messages containing `text` + `image_url` (base64 data URI) content parts.

**Internal pipeline**:
1. Load model once on startup: `load_pretrained_model(model_path, None, "llava_deepseekcoder")`
   - from ChartCoder's `llava/model/builder.py` (import via `sys.path.insert`)
2. For each request: decode base64 image → PIL Image → `process_images()`
3. Build prompt via `conv_templates["deepseekcoder"]` + `tokenizer_image_token()`
4. Run `model.generate()` with params from config (`temperature=0.1, top_p=0.95, max_new_tokens=2048`)
5. Return decoded text in OpenAI response envelope

**CLI**: `python serve/serve_chartcoder.py --model-path ./models/ChartCoder --chartcoder-repo ./ChartCoder --port 8080`

> **Environment note**: ChartCoder requires `torch==2.0.1` + `transformers==4.31.0`. Run `serve_chartcoder.py` in a separate conda env (`conda activate chartcoder_env`) where `ChartCoder/requirements.txt` is installed. All other scripts run in the standard project env.

---

### `inference/render.py`

Adopts ChartMimic's validated subprocess rendering approach.

**`render_chart_code(code: str, cfg: dict) -> bytes | None`**:

1. Strip any existing `plt.savefig(...)` and `plt.show()` lines via regex
2. Strip markdown fences (` ```python ... ``` `)
3. Write to a temp `.py` file; append:
   ```python
   import matplotlib
   matplotlib.use("Agg")
   plt.savefig("{tmp_output_path}", bbox_inches="{cfg.bbox_inches}")
   ```
4. Execute: `subprocess.run(["python3", tmp_script], timeout=cfg.timeout_sec, capture_output=True)`
5. If exit code == 0 and output file exists: read PNG bytes and return
6. On failure (exception, non-zero exit, timeout): log stderr snippet, return `None`

This mirrors `/chart2code/utils/post_process/code_interpreter.py` from ChartMimic.

---

### `inference/actor_client.py` and `inference/critic_client.py`

Both are thin HTTP clients over the OpenAI Chat Completions API. They read endpoint/param config from the YAML config object passed in. Retry logic (3 attempts, exponential backoff) and proxy-clearing (`_clear_proxies()`) follow the same pattern as `vincicoder_repurpose`.

**`actor_client.generate(target_image_b64, prompt_text, cfg) -> str | None`**
- Sends: `[text: prompt_text] + [image: target_image_b64]`
- Returns: raw text response (the generated code)

**`actor_client.refine(target_image_b64, previous_code, critic_feedback, cfg) -> str | None`**
- Sends: `[text: actor_refine_prompt.format(...)] + [image: target_image_b64]`
- Actor still sees the original target image for visual reference during refinement

**`critic_client.evaluate(current_image_b64, target_image_b64, cfg) -> str | None`**
- Sends: `[text: critic_user] + [image: current_image_b64] + [image: target_image_b64]`
- System prompt: `critic_system`
- Returns: raw string — either `"DONE"` or natural-language feedback

---

### `inference/actor_critic_loop.py`

**`run_loop(sample, cfg) -> LoopResult`**

```
Round 0 — Actor initial generation:
  code_0 = actor.generate(target_image, actor_initial_prompt)
  img_0  = render(code_0)
  if render fails → stopped_by="render_fail_round0", final_code=code_0

Round k (k = 1 .. max_rounds):
  feedback = critic.evaluate(img_{k-1}, target_image)
  if feedback.strip() == "DONE" → stopped_by="done", final_code=code_{k-1}

  code_k = actor.refine(target_image, code_{k-1}, feedback)
  img_k  = render(code_k)
  if render fails → stopped_by="render_fail", final_code=code_{k-1}

After max_rounds → stopped_by="max_rounds", final_code=code_{max_rounds}
```

**`LoopResult`** (dataclass):
```python
@dataclass
class LoopResult:
    example_id: str
    final_code: str
    stopped_by: str          # "done" | "max_rounds" | "render_fail_round0" | "render_fail"
    rounds_used: int
    per_round: list[RoundRecord]

@dataclass
class RoundRecord:
    round: int               # 0 = actor initial
    code: str
    render_ok: bool
    rendered_image_b64: str  # empty string if render_ok=False
    critic_feedback: str     # "" for round 0; "DONE" if stopped after this round
```

---

### `eval/metrics.py`

- **`compute_ssim(img_bytes_a: bytes, img_bytes_b: bytes) -> float`**
  - Resize both images to the same dimensions (use GT image size as reference)
  - Convert to grayscale
  - `skimage.metrics.structural_similarity(img_a_gray, img_b_gray)`
  - Returns 0.0 on any failure

- **`execution_ok(code: str, cfg: dict) -> bool`**
  - Calls `render_chart_code(code, cfg)` — returns True if not None

- **`summary_stats(results: list[dict]) -> dict`**
  - Computes mean SSIM, execution rate, improvement delta over baseline

---

### `eval/run_benchmark.py`

Runs two passes over the ChartMimic test set and writes results.

**Pass 1 — Baseline** (ChartCoder alone, round 0 only):
- `code = actor.generate(target_image)` → render → SSIM vs GT

**Pass 2 — Critic-assisted** (`run_loop()` for each sample):
- Takes `loop_result.final_code` → render → SSIM vs GT

**Output files** in `cfg.benchmark.output_dir`:
- `results_baseline.jsonl`: one record per sample with baseline metrics
- `results_critic.jsonl`: one record per sample with critic-loop metrics + per-round details
- `summary.txt`: printed summary table

**Per-record format** (both files share fields; critic file has additional fields):
```json
{
  "example_id": "...",
  "baseline_exec_ok": true,
  "baseline_ssim": 0.71,
  "critic_exec_ok": true,
  "critic_ssim": 0.79,
  "critic_rounds_used": 2,
  "critic_stopped_by": "done",
  "improvement_ssim": 0.08,
  "per_round": [...]
}
```

**Summary table** (printed to stdout and saved to `summary.txt`):
```
ChartMimic Evaluation  (N=600, max_rounds=3)
─────────────────────────────────────────────────
                     Baseline     +Critic      Δ
─────────────────────────────────────────────────
Execution Rate        88.5%        91.8%      +3.3%
SSIM (exec. only)      0.723        0.768     +0.045
SSIM (all samples)     0.640        0.701     +0.061
─────────────────────────────────────────────────
Critic DONE rate         —          49.1%
Avg. rounds used         —           1.7
─────────────────────────────────────────────────
```

---

### `run_validation.py`

CLI entry point that orchestrates the full pipeline.

```bash
uv run python run_validation.py \
  --config configs/default.yaml \
  --num-samples 100 \          # override benchmark.num_samples for quick testing
  --output ./results/
```

All overridable via CLI flags; config file provides defaults.

---

## Full Workflow

```
Step 1: Download benchmark
  uv run python setup/download_chartmimic.py

Step 2: Download ChartCoder model
  uv run python setup/download_chartcoder.py

Step 3: (One-time) Clone ChartCoder repo & set up its env
  git clone https://github.com/thunlp/ChartCoder.git ./ChartCoder
  conda create -n chartcoder_env python=3.10 -y
  conda activate chartcoder_env
  pip install -e ./ChartCoder
  pip install -e "./ChartCoder[train]"
  pip install flash-attn --no-build-isolation   # optional

Step 4: Launch ChartCoder server  [terminal A, chartcoder_env]
  conda activate chartcoder_env
  python serve/serve_chartcoder.py \
    --model-path ./models/ChartCoder \
    --chartcoder-repo ./ChartCoder \
    --port 8080

Step 5: Launch Qwen critic via vLLM  [terminal B]
  vllm serve /path/to/Qwen3.5-122B-A10B \
    --served-model-name Qwen/Qwen3.5-122B-A10B \
    --port 7001 --tensor-parallel-size 8

Step 6: Edit config if needed
  vim configs/default.yaml   # update actor.url, critic.url if not localhost

Step 7: Quick smoke-test (5 samples)
  uv run python run_validation.py --config configs/default.yaml --num-samples 5

Step 8: Full benchmark run
  uv run python run_validation.py --config configs/default.yaml

Step 9: Inspect results
  cat results/summary.txt
  # per-sample details in results/results_critic.jsonl
```

---

## Dependencies (`requirements.txt`)

```
# Core HTTP / API
httpx>=0.25
fastapi>=0.110
uvicorn>=0.27
pyyaml>=6.0

# Data
datasets>=2.18
pandas>=2.0
Pillow>=10.0

# Metrics
scikit-image>=0.21

# ChartCoder server deps (install in chartcoder_env from ChartCoder/requirements.txt)
# torch==2.0.1, transformers==4.31.0, peft, accelerate
```

---

## Evaluation Note

ChartMimic's own evaluation pipeline uses **semantic code-level metrics** (text F1, chart-type F1, color Delta-E, layout F1) rather than SSIM. Our validation uses SSIM + execution rate as fast proxy metrics sufficient for hypothesis testing. If results are promising, a follow-up evaluation using ChartMimic's official evaluation scripts (`/chart2code/main.py`) can produce numbers directly comparable to published baselines.

---

## Expected Outcomes

| Result | Interpretation | Next Step |
|---|---|---|
| SSIM improves ≥ 0.02 on average | Hypothesis validated | Proceed to training critic with `generate_critic_data.py` |
| Execution rate improves ≥ 2% | Partial validation | Inspect failure modes; iterate on prompts in config YAML |
| No improvement or regression | Hypothesis not supported | Diagnose via per-round JSONL; check prompt design, rendering mismatch, domain gap |
