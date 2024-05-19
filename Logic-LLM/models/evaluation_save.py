import json
import os
from evaluation import evaluate_QA
import model_globals

def full_evaluation_save():
    results_json = {}

    backup = "random"
    split = model_globals.SPLIT_USED_IN_PAPER
    # now only saving Gemini results
    for model_name in model_globals.GEMINI_MODEL_NAMES:
        results_json[model_name] = {}
        for dataset_name in model_globals.DATASET_NAMES:
            result_path = f'./outputs/logic_inference'
            result_file = os.path.join(result_path, f'{dataset_name}_{split}_{model_name}_backup-{backup}.json')
            if os.path.isfile(result_file):
                with open(result_file, 'r') as f:
                    all_samples = json.load(f)
                executable_samples = [sample for sample in all_samples if sample['flag'] == 'success']
                
                overall_accuracy = evaluate_QA(all_samples)
                executable_rate = len(executable_samples) / len(all_samples) if all_samples else 0
                executable_accuracy = evaluate_QA(executable_samples)
                
                results_json[model_name][dataset_name] = {
                    "Overall_Accuracy": overall_accuracy,
                    "Executable_Rate": executable_rate,
                    "Executable_Accuracy": executable_accuracy,
                }
            else:
                print(f"No results available for {model_name} on {dataset_name}")
    
    outputs_path = f'./outputs'
    eval_path = os.path.join(outputs_path, "evaluation", 'evaluation_logic_programs.json')
    with open(eval_path, 'w') as file:
        json.dump(results_json, file, indent=4)

if __name__ == "__main__":
    full_evaluation_save()

    