models=(
    "gpt-4o"
)

for model in "${models[@]}"; do
    python3 chart2code/main.py \
    --cfg_path eval_configs/direct_generation_proprietary.yaml \
    --tasks chart2code \
    --model ${model}
done
