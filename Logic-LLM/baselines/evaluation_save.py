import json
import os
import model_globals
from evaluation import get_answer_options
import re

def evaluate_QA_gemini_save(QA_results, answer_options):
    total_em = 0.0
    total_f1 = 0.0
    count = 0
    
    for sample in QA_results:
        gold_answer = sample['answer'].replace('(', '').replace(')', '').strip()
        answer_str = sample['predicted_answer'].strip()

        prediction = re.search(rf'(?<=\s|[^a-zA-Z0-9])[{answer_options}](?=\s|[^a-zA-Z0-9])', answer_str)
        if prediction:
            prediction =prediction.group(0)
        
        em_score = 1.0 if prediction == gold_answer else 0.0
        total_em += em_score
        count += 1
    
    avg_em = total_em / count
    return avg_em


def full_evaluation_save():
    results_json = {}

    split = model_globals.SPLIT_USED_IN_PAPER
    # now only saving Gemini results
    for model_name in model_globals.GEMINI_MODEL_NAMES:
        results_json[model_name] = {}
        for dataset_name in model_globals.DATASET_NAMES:
            answer_options = get_answer_options(dataset_name)
            results_json[model_name][dataset_name] = {}
            for mode in model_globals.MODES:
                result_path = './baselines/results'
                result_file = os.path.join(result_path, f'{mode}_{dataset_name}_{split}_{model_name}.json')
                if os.path.isfile(result_file):
                    with open(result_file, 'r') as f:
                        all_samples = json.load(f)
                    
                    avg_em = evaluate_QA_gemini_save(all_samples, answer_options)
                    
                    results_json[model_name][dataset_name][mode] = {
                        "Average_EM_score": avg_em,
                    }
                else:
                    print(f"No results available for {model_name} on {dataset_name} with {mode}")
    
    outputs_path = f"./baselines/evaluation"
    eval_path = os.path.join(outputs_path, 'evaluation_baselines.json')

    with open(eval_path, 'w') as file:
        json.dump(results_json, file, indent=4)

if __name__ == "__main__":
    full_evaluation_save()

    