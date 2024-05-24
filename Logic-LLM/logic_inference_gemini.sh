#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate solver2

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")
model_names=("gemini-1.0-pro-vision-001" "gemini-1.5-pro-preview-0409" "gemini-1.5-pro-preview-0514" "gemini-1.5-flash-preview-0514")
# gemini_model="gemini-1.0-pro-vision-001"
# gemini_model="gemini-1.5-pro-preview-0409"
# gemini_model="gemini-1.5-pro-preview-0514"
# gemini_model="gemini-1.5-flash-preview-0514"

for gemini_model in "${model_names[@]}"
    do
        for task in "${tasks[@]}"
            do
                echo "Running program with task: $task"
                python3 ./models/logic_inference.py \
                    --model_name "$gemini_model" \
                    --dataset_name "$task" \
                    --split dev \
                    --backup_strategy LLM \
                    --backup_LLM_result_path "./baselines/results/CoT_${task}_dev_gemini-1.5-flash-preview-0514.json"
            done
    done