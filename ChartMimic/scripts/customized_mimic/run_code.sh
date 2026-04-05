models=(
  "gpt-4o"
)

template_type=edit;agent_type=EditAgent

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_checker.py \
    --input_file results/customized/chartedit_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_interpreter.py \
    --input_file results/customized/chartedit_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done

for model in "${models[@]}"; do
    python chart2code/utils/post_process/convert_pdf2png.py \
    --dir_path results/customized/chartedit_${model}_${agent_type}_results/${template_type}
done
