#!/bin/bash

#eval "$(conda shell.bash hook)"
#conda deactivate
#conda activate DL2

#tasks=("sudoku_fill_in" "graph_fill_in" "graph_validity" "sudoku_validity" "set_validity")
tasks=("sudoku_validity" "set_validity")
#tasks=("sudoku_validity")
#tasks=("graph_fill_in" "sudoku_fill_in")

#gemini_model="gemini-1.5-pro-preview-0409"
claude_model="claude-3-haiku@20240307"
gemini_model="gemini-1.5-flash-preview-0514"
gpt_model="gpt-4"

for task in "${tasks[@]}"
    do
        echo "Running program with task: $task"
        python ./models/logic_program.py \
            --dataset_name "$task" \
            --split data \
            --model_name "$gemini_model" \
            --max_new_tokens 1024
    done