#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate DL2


# gemini_model="gemini-1.0-pro-vision-001"
# gemini_model="gemini-1.5-pro-preview-0409"
# gemini_model="gemini-1.5-pro-preview-0514"
gemini_model="gemini-1.5-flash-preview-0514"

orders=("test_first_choice_correct" "test_second_choice_correct" "test_third_choice_correct" "test_fourth_choice_correct" "test_fifth_choice_correct")

for split in "${orders[@]}"
    do
        echo "Running program in direct mode with split: $split"
        python3 evaluation.py \
            --model_name "$gemini_model" \
            --dataset_name AR-LSAT \
            --split "$split" \
            --mode Direct
    done

# for split in "${orders[@]}"
#     do
#         echo "Running program in direct mode with split: $split"
#         python3 gemini_baseline.py \
#             --model_name "$gemini_model" \
#             --dataset_name AR-LSAT \
#             --split "$split" \
#             --mode CoT \
#             --max_new_tokens 1024
#     done