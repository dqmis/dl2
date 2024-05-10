"""
Dataset wrapper for MathVision, adapted from its eval_scripts/gpt-4v.py file.
"""

import csv

from dataset_wrapper import DatasetWrapper


class Rebus(DatasetWrapper):
    def __init__(self, data_file="data.json"):
        self.root_folder = "data/rebus"
        self.root_data_dir = ""
        self.output_dir = "outputs"
        self.data_file = data_file

        self.data = self.load_data()

    def load_data(self):
        rows = []
        input_file = f"{self.root_folder}/{self.root_data_dir}/{self.data_file}"

        with open(input_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            headers = next(csv_reader)

            for row in csv_reader:
                rows.append(row)

        return rows

    def evaluate(self):
        def prompt_func(category):
            return f"This rebus puzzle is a play on words based on images, and may contain text, logical operators, addition/subtraction of letters, and other forms of creative thinking to solve. Can you figure out what it is? The category for this puzzle is {category}; that is, your answer should match the category in order to be correct.\n\nTake a deep breath, and let's begin. You can think for as long as you want, until you get a correct answer in the category {category}. When you're done reasoning and thinking, output your final answer in three braces, like {{{{{{this}}}}}}.\n"

        for i in range(len(self.data)):
            current_row = self.data[i]
            filename = current_row[0]
            correct_answer = current_row[1]
            also_correct_answer = current_row[2]
            category = current_row[3]

            prompt = prompt_func(category)
            url = f"https://cavendishlabs.org/rebus/images/{filename}"
            yield prompt, None, url

            # messages = [
            #     {
            #         "role": "user",
            #         "content": [
            #             {"type": "text", "text": prompt},
            #             {
            #                 "type": "image_url",
            #                 "image_url": {
            #                     "url": url,
            #                 },
            #             },
            #         ],
            #     }
            # ]

            # yield messages
