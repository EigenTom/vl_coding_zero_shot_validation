#!/usr/bin/env bash
# =============================================================================
# Zero-Shot Actor-Critic Validation — One-Click Setup
# =============================================================================
# 用法:  bash setup.sh [--skip-qwen]
#
# 前置条件:
#   - Linux x86_64, NVIDIA GPU (Ampere+), CUDA 12.x 驱动已安装
#   - uv (https://docs.astral.sh/uv/getting-started/installation/)
#   - git, wget/curl, unzip
#
# 本脚本会:
#   0. 初始化 git submodule (ChartCoder)
#   1. 检查 ChartMimic 补充材料 (已包含在仓库中)
#   2. 为 ChartCoder 创建 venv 并安装依赖 (torch + flash-attn)
#   3. 下载 ChartCoder 模型权重
#   4. 下载 SigLip 视觉编码器并更新 config.json
#   5. 为主项目创建 venv 并安装依赖
#   6. (可选) 为 Qwen 3.5 Critic 创建 venv
#   7. 准备 ChartMimic 评测数据 (JSONL)
# =============================================================================
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

# ── Parse flags ──────────────────────────────────────────────────────────────
SKIP_QWEN=false
for arg in "$@"; do
    case "$arg" in
        --skip-qwen) SKIP_QWEN=true ;;
    esac
done

# ── Helper ───────────────────────────────────────────────────────────────────
info()  { echo -e "\n\033[1;34m[INFO]\033[0m $*"; }
ok()    { echo -e "\033[1;32m[OK]\033[0m $*"; }
warn()  { echo -e "\033[1;33m[WARN]\033[0m $*"; }
err()   { echo -e "\033[1;31m[ERROR]\033[0m $*" >&2; }

require_cmd() {
    command -v "$1" &>/dev/null || { err "需要 $1，请先安装"; exit 1; }
}

# ── Pre-flight checks ───────────────────────────────────────────────────────
require_cmd uv
require_cmd git
require_cmd python3.10

# Detect CUDA version from nvcc or nvidia-smi
detect_cuda_major() {
    if command -v nvcc &>/dev/null; then
        nvcc --version 2>/dev/null | grep -oP 'release \K[0-9]+' | head -1
    elif command -v nvidia-smi &>/dev/null; then
        nvidia-smi 2>/dev/null | grep -oP 'CUDA Version: \K[0-9]+' | head -1
    fi
}

CUDA_MAJOR=$(detect_cuda_major)
if [[ "$CUDA_MAJOR" -ge 12 ]] 2>/dev/null; then
    TORCH_INDEX="https://download.pytorch.org/whl/cu121"
    info "检测到 CUDA 12.x，使用 torch+cu121"
elif [[ "$CUDA_MAJOR" -ge 11 ]] 2>/dev/null; then
    TORCH_INDEX="https://download.pytorch.org/whl/cu118"
    info "检测到 CUDA 11.x，使用 torch+cu118"
else
    warn "未检测到 CUDA 版本，默认使用 cu121"
    TORCH_INDEX="https://download.pytorch.org/whl/cu121"
fi

# ═════════════════════════════════════════════════════════════════════════════
# Step 0: Git submodule
# ═════════════════════════════════════════════════════════════════════════════
info "Step 0: 初始化 git submodules ..."
git submodule update --init --recursive
ok "ChartCoder submodule 已就绪"

# ═════════════════════════════════════════════════════════════════════════════
# Step 1: 检查 ChartMimic 补充材料 (已包含在仓库中)
# ═════════════════════════════════════════════════════════════════════════════
CHARTMIMIC_SUPP_DIR="$ROOT_DIR/ChartMimic"

info "Step 1: 检查 ChartMimic 补充材料 ..."
if [[ -d "$CHARTMIMIC_SUPP_DIR/dataset" ]]; then
    ok "ChartMimic 补充材料已就绪: $CHARTMIMIC_SUPP_DIR"
else
    err "ChartMimic 补充材料不存在: $CHARTMIMIC_SUPP_DIR/dataset"
    err "请确认仓库克隆完整 (ChartMimic/ 目录应已包含在仓库中)"
    exit 1
fi

# ═════════════════════════════════════════════════════════════════════════════
# Step 3: ChartCoder venv
# ═════════════════════════════════════════════════════════════════════════════
CHARTCODER_DIR="$ROOT_DIR/ChartCoder"
CHARTCODER_VENV="$CHARTCODER_DIR/.venv"

info "Step 3: 为 ChartCoder 创建 venv 并安装依赖 ..."
if [[ ! -f "$CHARTCODER_VENV/bin/python" ]]; then
    uv venv "$CHARTCODER_VENV" --python 3.10
fi

CCPYTHON="$CHARTCODER_VENV/bin/python"

# 安装 torch (与系统 CUDA 匹配)
info "  安装 torch (cu121) ..."
uv pip install --python "$CCPYTHON" \
    torch==2.5.1 torchvision==0.20.1 \
    --index-url "$TORCH_INDEX"

# 安装 ChartCoder 包 (editable)
info "  安装 ChartCoder (llava) ..."
uv pip install --python "$CCPYTHON" -e "$CHARTCODER_DIR"

# 安装 transformers 和推理所需包
info "  安装 transformers + inference deps ..."
uv pip install --python "$CCPYTHON" \
    "transformers>=4.40" \
    accelerate \
    fastapi "uvicorn[standard]" \
    Pillow shortuuid einops ftfy \
    sentencepiece tokenizers \
    setuptools

# 确保 pkg_resources 可用 (flash-attn 编译需要)
if ! "$CCPYTHON" -c "import pkg_resources" 2>/dev/null; then
    SYS_PKG_RES=$(python3.10 -c "import pkg_resources, os; print(os.path.dirname(pkg_resources.__file__))" 2>/dev/null || true)
    if [[ -n "$SYS_PKG_RES" && -d "$SYS_PKG_RES" ]]; then
        SITE_PACKAGES=$("$CCPYTHON" -c "import site; print(site.getsitepackages()[0])")
        ln -sf "$SYS_PKG_RES" "$SITE_PACKAGES/pkg_resources"
        info "  已链接系统 pkg_resources"
    fi
fi

# 编译安装 flash-attn
info "  编译 flash-attn (可能需要 5-10 分钟) ..."
if "$CCPYTHON" -c "import flash_attn" 2>/dev/null; then
    ok "  flash-attn 已安装"
else
    uv pip install --python "$CCPYTHON" flash-attn --no-build-isolation
    ok "  flash-attn 编译完成"
fi

ok "ChartCoder venv 就绪: $CHARTCODER_VENV"

# ═════════════════════════════════════════════════════════════════════════════
# Step 4: 下载 ChartCoder 模型权重
# ═════════════════════════════════════════════════════════════════════════════
MODEL_DIR="$ROOT_DIR/models/ChartCoder"
info "Step 4: 下载 ChartCoder 模型权重 ..."

if [[ -f "$MODEL_DIR/model.safetensors.index.json" ]] && ls "$MODEL_DIR"/*.safetensors &>/dev/null; then
    ok "ChartCoder 权重已存在: $MODEL_DIR"
else
    "$CCPYTHON" -c "
from huggingface_hub import snapshot_download
import os
endpoint = os.environ.get('HF_ENDPOINT', 'https://huggingface.co')
print(f'从 {endpoint} 下载 xxxllz/ChartCoder ...')
snapshot_download(
    repo_id='xxxllz/ChartCoder',
    local_dir='$MODEL_DIR',
    local_dir_use_symlinks=False,
)
print('下载完成')
"
    ok "ChartCoder 权重已下载: $MODEL_DIR"
fi

# ═════════════════════════════════════════════════════════════════════════════
# Step 5: 下载 SigLip 并更新 config.json
# ═════════════════════════════════════════════════════════════════════════════
SIGLIP_DIR="$ROOT_DIR/models/siglip-so400m-patch14-384"
info "Step 5: 下载 SigLip 视觉编码器 ..."

if [[ -f "$SIGLIP_DIR/model.safetensors" ]]; then
    ok "SigLip 已存在: $SIGLIP_DIR"
else
    "$CCPYTHON" -c "
from huggingface_hub import snapshot_download
import os
endpoint = os.environ.get('HF_ENDPOINT', 'https://huggingface.co')
print(f'从 {endpoint} 下载 google/siglip-so400m-patch14-384 ...')
snapshot_download(
    repo_id='google/siglip-so400m-patch14-384',
    local_dir='$SIGLIP_DIR',
    local_dir_use_symlinks=False,
)
print('下载完成')
"
    ok "SigLip 已下载: $SIGLIP_DIR"
fi

# 更新 config.json 中的 mm_vision_tower 路径
info "  更新 ChartCoder config.json 中的 vision_tower 路径 ..."
"$CCPYTHON" -c "
import json
config_path = '$MODEL_DIR/config.json'
with open(config_path) as f:
    cfg = json.load(f)
cfg['mm_vision_tower'] = '$SIGLIP_DIR'
with open(config_path, 'w') as f:
    json.dump(cfg, f, indent=2)
print(f'已更新 mm_vision_tower → {cfg[\"mm_vision_tower\"]}')
"
ok "config.json 已更新"

# ═════════════════════════════════════════════════════════════════════════════
# Step 6: 主项目 venv
# ═════════════════════════════════════════════════════════════════════════════
MAIN_VENV="$ROOT_DIR/.venv"
info "Step 6: 为主项目创建 venv ..."

if [[ ! -f "$MAIN_VENV/bin/python" ]]; then
    uv venv "$MAIN_VENV" --python 3.10
fi

MAIN_PYTHON="$MAIN_VENV/bin/python"
uv pip install --python "$MAIN_PYTHON" -r "$ROOT_DIR/requirements.txt"
uv pip install --python "$MAIN_PYTHON" matplotlib
ok "主项目 venv 就绪: $MAIN_VENV"

# ═════════════════════════════════════════════════════════════════════════════
# Step 7: (可选) Qwen 3.5 Critic venv
# ═════════════════════════════════════════════════════════════════════════════
if $SKIP_QWEN; then
    warn "跳过 Qwen Critic 环境 (--skip-qwen)"
else
    QWEN_VENV="$ROOT_DIR/.venv_qwen"
    info "Step 7: 为 Qwen 3.5 Critic (vLLM) 创建 venv ..."

    if [[ ! -f "$QWEN_VENV/bin/python" ]]; then
        uv venv "$QWEN_VENV" --python 3.10
    fi

    QWEN_PYTHON="$QWEN_VENV/bin/python"
    uv pip install --python "$QWEN_PYTHON" \
        vllm \
        --index-url "$TORCH_INDEX"
    ok "Qwen vLLM venv 就绪: $QWEN_VENV"
fi

# ═════════════════════════════════════════════════════════════════════════════
# Step 8: 准备 ChartMimic 评测数据
# ═════════════════════════════════════════════════════════════════════════════
DATASET_FILE="$ROOT_DIR/data/chartmimic/test.jsonl"
info "Step 8: 准备 ChartMimic 评测数据 ..."

if [[ -f "$DATASET_FILE" ]] && [[ -s "$DATASET_FILE" ]]; then
    ok "评测数据已存在: $DATASET_FILE"
else
    # 更新 configs/default.yaml 中的 chartmimic.supp_dir
    sed -i "s|supp_dir:.*|supp_dir: \"$CHARTMIMIC_SUPP_DIR\"|" "$ROOT_DIR/configs/default.yaml"

    "$MAIN_PYTHON" "$ROOT_DIR/setup/download_chartmimic.py" \
        --supp-dir "$CHARTMIMIC_SUPP_DIR" \
        --output "$DATASET_FILE"
    ok "评测数据已生成: $DATASET_FILE"
fi

# ═════════════════════════════════════════════════════════════════════════════
# Done
# ═════════════════════════════════════════════════════════════════════════════
echo ""
echo "============================================================"
echo "  环境搭建完成!"
echo "============================================================"
echo ""
echo "  ChartCoder venv : $CHARTCODER_VENV"
echo "  主项目 venv      : $MAIN_VENV"
echo "  ChartCoder 模型  : $MODEL_DIR"
echo "  SigLip 模型      : $SIGLIP_DIR"
echo "  评测数据          : $DATASET_FILE"
echo ""
echo "  启动 ChartCoder 服务 (指定 GPU):"
echo "    CUDA_VISIBLE_DEVICES=3 $CCPYTHON \\"
echo "      serve/serve_chartcoder.py \\"
echo "      --model-path $MODEL_DIR \\"
echo "      --chartcoder-repo $CHARTCODER_DIR \\"
echo "      --port 8080"
echo ""
echo "  运行 baseline 评测 (不含 critic):"
echo "    $MAIN_PYTHON run_validation.py --config configs/default.yaml \\"
echo "      --num-samples 5 --skip-critic"
echo ""
echo "  如需使用 HuggingFace 镜像，设置:"
echo "    export HF_ENDPOINT=https://hf-mirror.com"
echo "============================================================"
