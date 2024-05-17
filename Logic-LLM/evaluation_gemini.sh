#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate solver2

tasks=("ProntoQA" "ProofWriter" "FOLIO" "LogicalDeduction" "AR-LSAT")

# gemini_model="gemini-1.5-pro-preview-0409"
# gemini_model="gemini-1.0-pro-vision-001"
gemini_model="gemini-1.5-pro-preview-0514"


for task in "${tasks[@]}"
    do
        echo "Running program with task: $task"
        python3 ./models/evaluation.py \
            --model_name "$gemini_model" \
            --dataset_name "$task" \
            --split dev \
            --backup random    
    done