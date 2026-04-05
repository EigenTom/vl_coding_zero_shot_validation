<div align="center">
<h1> ChartMimic: Evaluating LMM’s Cross-Modal Reasoning Capability via Chart-to-Code Generation
 </h1>
</div>

## 🚀 Quick Start

Here we provide a quick start guide to evaluate LMMs on ChartMimic.

### Setup Environment

```shell
conda env create -f environment.yaml
conda activate chartmimic
```

Set up the environment variables in `.env` file.

```shell
PROJECT_PATH=${YOUR_PROJECT_PATH}
OPENAI_BASE_URL=${YOUR_OPEN_AI_BASE_URL}
OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}
ANTHROPIC_API_KEY=${YOUR_ANTHROPIC_API_KEY}
GOOGLE_API_KEY=${YOUR_ANTHROPIC_API_KEY}
```

### Evaluate Models

#### Task 1: Direct Mimic

Example script for `gpt-4o` on the `Direct Mimic` task (testmini):

```shell
export PROJECT_PATH=${YOUR_PROJECT_PATH}

# Step 1: Get Model Reponse
bash scripts/direct_mimic/run_generation.sh

# Step 2: Run the Code in the Response
bash scripts/direct_mimic/run_code.sh

# Step 3: Get Lowlevel Score
bash scripts/direct_mimic/run_evaluation_lowlevel.sh

# Step 4: Get Highlevel Score
bash scripts/direct_mimic/run_evaluation_highlevel.sh
```

#### Task 2: Customized Mimic

Example script for `gpt-4o` on the `Customized Mimic` task (testmini):

```shell
export PROJECT_PATH=${YOUR_PROJECT_PATH}

# Step 1: Get Model Reponse
bash scripts/customized_mimic/run_generation.sh

# Step 2: Run the Code in the Response
bash scripts/customized_mimic/run_code.sh

# Step 3: Get Lowlevel Score
bash scripts/customized_mimic/run_evaluation_lowlevel.sh

# Step 4: Get Highlevel Score
bash scripts/customized_mimic/run_evaluation_highlevel.sh
```

#### Different LMMs

We now offer configuration for 17 SOTA LMM models (`gpt-4o`, `claude-3-opus-20240229`, `gemini-pro-vision`, `IDEFICS2-8B`,`DeepSeek-VL-7B`,`LLaVA-Next-Yi-34B`,`LLaVA-Next-Mistral-7B`,`Qwen2-VL-2B`,`Cogvlm2-llama3-chat-19B`,`InternVL2-2B`,`Qwen2-VL-7B`,`InternVL2-4B`,`InternVL2-8B`,`MiniCPM-Llama3-V-2.5`,`Phi-3-Vision-128K`,`InternVL2-26B` and `InternVL2-Llama3-76B`)

## 📚 Data

The file structure of evaluation data is as follows:

```
.
├── customized_1800/ # Data for Customized Mimic (test)
├── customized_600/  # Data for Customized Mimic (testmini)
├── direct_1800/  # Data for Direct Mimic (test)
└── direct_600/  # Data for Direct Mimic (testmini)
```