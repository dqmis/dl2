#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate solver2

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")

# gemini_model="gemini-1.0-pro-vision-001"
# gemini_model="gemini-1.5-pro-preview-0409"
# gemini_model="gemini-1.5-pro-preview-0514"
gemini_model="gemini-1.5-flash-preview-0514"


for task in "${tasks[@]}"
    do
        echo "Running program in direct mode with task: $task"
        python3 gemini_baseline.py \
            --model_name "$gemini_model" \
            --dataset_name "$task" \
            --split dev \
            --mode Direct \
            --max_new_tokens 16
    done

for task in "${tasks[@]}"
    do
        echo "Running program in CoT mode with task: $task"
        python3 gemini_baseline.py \
            --model_name "$gemini_model" \
            --dataset_name "$task" \
            --split dev \
            --mode CoT \
            --max_new_tokens 1024
    done