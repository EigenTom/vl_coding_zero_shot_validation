models=(
    "gpt-4o"
)

for model in "${models[@]}"; do
    python chart2code/main.py \
    --cfg eval_configs/customized_generation.yaml \
    --tasks chartedit \
    --model ${model}
done
