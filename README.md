# Zero-Shot Actor-Critic 图表代码生成验证

基于 [ChartCoder](https://github.com/thunlp/ChartCoder) 和 [ChartMimic](https://openreview.net/forum?id=sGpCzsfd1K) 的零样本图表代码生成 Actor-Critic 验证框架。

## 概述

本项目实现了一个两阶段评测流程:

1. **Baseline (Actor-only)**: ChartCoder 直接根据图表图片生成 Matplotlib 代码
2. **Critic-assisted**: ChartCoder 生成代码后，Qwen 3.5-122B 作为视觉 Critic 比较渲染结果和目标图表，提供反馈让 Actor 迭代修正

## 项目结构

```
vl_coding_zero_shot_validation/
├── setup.sh                    # 一键环境搭建脚本
├── run_validation.py           # 评测入口
├── configs/
│   └── default.yaml            # 所有配置 (端点、提示词、参数)
├── serve/
│   └── serve_chartcoder.py     # ChartCoder OpenAI 兼容 API 服务
├── inference/
│   ├── actor_client.py         # Actor API 客户端
│   ├── critic_client.py        # Critic API 客户端
│   ├── actor_critic_loop.py    # Actor-Critic 循环逻辑
│   └── render.py               # Matplotlib 代码渲染器
├── eval/
│   ├── run_benchmark.py        # 评测主循环
│   ├── metrics.py              # 评测指标
│   └── chartmimic_evaluator.py # ChartMimic 官方语义评测封装
├── setup/
│   ├── download_chartcoder.py  # 下载 ChartCoder 模型
│   └── download_chartmimic.py  # 准备 ChartMimic 评测数据
├── ChartCoder/                 # git submodule (thunlp/ChartCoder)
├── ChartMimic/                 # 动态下载的补充材料 (已 gitignore)
├── models/                     # 模型权重目录 (已 gitignore)
└── data/                       # 评测数据 (已 gitignore)
```

## 环境要求

- Linux x86_64
- NVIDIA GPU (Ampere 及以上), CUDA 12.x 驱动
- Python 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- git, wget, unzip

## 快速开始

### 1. 克隆仓库

```bash
git clone --recursive <repo-url>
cd vl_coding_zero_shot_validation
```

### 2. 一键搭建环境

```bash
# 如需使用 HuggingFace 镜像 (国内推荐):
export HF_ENDPOINT=https://hf-mirror.com

# 完整安装 (包含 ChartMimic 数据下载 + Qwen vLLM 环境)
bash setup.sh

# 仅安装 ChartCoder 相关 (跳过 ChartMimic 下载和 Qwen 环境)
bash setup.sh --skip-chartmimic --skip-qwen
```

脚本会自动完成:
- 初始化 git submodule (ChartCoder)
- 下载并解压 ChartMimic 补充材料
- 创建 ChartCoder 独立 venv，安装 torch + flash-attn
- 下载 ChartCoder 模型权重 (~14GB)
- 下载 SigLip 视觉编码器 (~3.3GB) 并更新 config.json
- 创建主项目 venv
- (可选) 创建 Qwen vLLM 服务环境
- 准备 ChartMimic 评测数据 (JSONL)

### 3. 启动 ChartCoder 服务

```bash
# 指定 GPU (例如 GPU 3)
CUDA_VISIBLE_DEVICES=3 ChartCoder/.venv/bin/python \
    serve/serve_chartcoder.py \
    --model-path models/ChartCoder \
    --chartcoder-repo ChartCoder \
    --port 8080
```

验证服务:
```bash
curl http://localhost:8080/health
# {"status":"ok","model_loaded":true}
```

### 4. (可选) 启动 Qwen Critic 服务

```bash
CUDA_VISIBLE_DEVICES=0,1,2 .venv_qwen/bin/python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen3.5-122B-A10B \
    --port 7001 \
    --tensor-parallel-size 3
```

### 5. 运行评测

```bash
# 快速冒烟测试 (5 样本, 仅 baseline)
.venv/bin/python run_validation.py \
    --config configs/default.yaml \
    --num-samples 5 \
    --skip-critic

# 完整 baseline 评测
.venv/bin/python run_validation.py \
    --config configs/default.yaml \
    --skip-critic

# 完整 Actor-Critic 评测 (需启动 Qwen Critic 服务)
.venv/bin/python run_validation.py \
    --config configs/default.yaml

# 自定义端点
.venv/bin/python run_validation.py \
    --config configs/default.yaml \
    --actor-url http://localhost:8080 \
    --critic-url http://localhost:7001 \
    --num-samples 50 \
    --output ./results/run_001
```

## 配置说明

所有配置集中在 `configs/default.yaml`:

| 配置项 | 说明 |
|--------|------|
| `actor.url` | ChartCoder API 地址 (默认 `http://localhost:8080`) |
| `critic.url` | Qwen Critic API 地址 (默认 `http://localhost:7001`) |
| `loop.max_rounds` | Critic 最大迭代轮数 (默认 3) |
| `benchmark.dataset` | 评测数据路径 |
| `benchmark.num_samples` | 评测样本数 (-1 = 全部) |

## 常见问题

**Q: HuggingFace 下载慢/超时?**
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

**Q: flash-attn 编译失败?**
- 确保系统 CUDA 版本与 torch 的 CUDA 版本匹配
- 需要 `pkg_resources` (来自 setuptools)，脚本会自动处理

**Q: 模型加载时报 SigLip 路径错误?**
- 确认 `models/ChartCoder/config.json` 中 `mm_vision_tower` 指向正确的本地 SigLip 路径
- `setup.sh` 会自动更新此路径

**Q: 如何只跑 Baseline 不跑 Critic?**
```bash
.venv/bin/python run_validation.py --config configs/default.yaml --skip-critic
```
