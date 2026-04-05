models=(
    "gpt-4o"
)
for model in "${models[@]}"; do
    evaluation_dir=results/direct/chart2code_${model}_DirectAgent_results/direct
    python3 chart2code/main.py --cfg_path eval_configs/direct/gpt4evaluation.yaml --tasks gpt4evaluation --evaluation_dir ${evaluation_dir}
done