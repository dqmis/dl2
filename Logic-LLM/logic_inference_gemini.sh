#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate solver2

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")
backup_strategies=("random" "Direct" "CoT")
model_names=("gemini-1.0-pro-vision-001" "gemini-1.5-pro-preview-0409" "gemini-1.5-pro-preview-0514" "gemini-1.5-flash-preview-0514")


for backup in "${backup_strategies[@]}"
    do
    if [[ "$backup" == "random" ]]
        then
            backup_strat="random"
        else
            backup_strat="LLM"
        fi
    for gemini_model in "${model_names[@]}"
        do
            for task in "${tasks[@]}"
                do
                    echo "Running program with task: $task"
                    python3 ./models/logic_inference.py \
                        --model_name "$gemini_model" \
                        --dataset_name "$task" \
                        --split dev \
                        --backup_strategy "$backup_strat" \
                        --backup_LLM_result_path "./baselines/results/${backup}_${task}_dev_${gemini_model}.json"
                done
        done
    done