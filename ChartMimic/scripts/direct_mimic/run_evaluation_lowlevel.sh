models=(
    "gpt-4o"
)

dataset=direct_600

for model in "${models[@]}"; do
    python3 chart2code/main.py --cfg eval_configs/direct/code4evaluation.yaml --tasks code4evaluation --model "${model}" > code4evaluation_direct_${model}.log 2>&1
done