#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate DL2

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")

gemini_model="gemini-1.5-pro-preview-0409"
# gemini_model="gemini-1.0-pro-vision-001"

for task in "${tasks[@]}"
    do
        echo "Running program with task: $task"
        python3 ./models/logic_program.py \
            --dataset_name "$task" \
            --split dev \
            --model_name "$gemini_model" \
            --max_new_tokens 1024
    done