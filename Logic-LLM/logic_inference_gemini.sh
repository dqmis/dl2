#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate solver

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")

gemini_model="gemini-1.5-pro-preview-0409"

for task in "${tasks[@]}"
    do
        echo "Running program with task: $task"
        python3 ./models/logic_inference.py \
            --model_name "$gemini_model" \
            --dataset_name "$task" \
            --split dev \
            --backup_strategy random
    done