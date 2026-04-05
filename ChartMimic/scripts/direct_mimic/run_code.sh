models=(
    "gpt-4o"
)

dataset=direct_600

template_type=direct;agent_type=DirectAgent

for model in "${models[@]}"; do
    python3 chart2code/utils/post_process/code_checker.py \
        --input_file results/${dataset}/chart2code_${model}_${agent_type}_results.json \
        --template_type ${template_type}

    python3 chart2code/utils/post_process/code_interpreter.py \
        --input_file results/${dataset}/chart2code_${model}_${agent_type}_results.json \
        --template_type ${template_type}

    python3 chart2code/utils/post_process/convert_pdf2png.py \
        --dir_path results/${dataset}/chart2code_${model}_${agent_type}_results/${template_type}
done
