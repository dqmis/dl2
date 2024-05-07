"""
Dataset wrapper for MathVision, adapted from its models/GPT4.py file.
"""

import json

from dataset_wrapper import DatasetWrapper

from data.MathVision.models.GPT4 import geninput, load_jsonl


class MathVision(DatasetWrapper):
    def __init__(self, data_dir):
        self.root_folder = "data/MathVision"
        self.root_data_dir = "data"
        self.output_dir = "outputs"
        self.data_dir = data_dir

    def evaluate(self, model):
        data = load_jsonl(
            f"{self.root_folder}/{self.root_data_dir}{self.data_dir}.json")

        for point in data:
            question = geninput(point)

            for i in range(10):
                question = question.replace(f'<image{i}>', '').strip()

            response = model(question)
            response['input'] = question
            response['extra'] = point
            path_out = f"{self.root_folder}/{self.output_dir}/"\
                "{self.data_dir}.jsonl"

            with open(path_out, 'a') as f:
                f.write(json.dumps(response, ensure_ascii=False)+'\n')
