"""
Dataset wrapper for AlgoPuzzleVQA, adapted from its main.py file.
"""

from tqdm import tqdm

from dataset_wrapper import DatasetWrapper

from LLM_PuzzleTest.AlgoPuzzleVQA.data_loading import (
    Data, convert_text_to_image, convert_image_to_text)
from LLM_PuzzleTest.AlgoPuzzleVQA.modeling import EvalModel
from LLM_PuzzleTest.AlgoPuzzleVQA.prompting import select_prompter



class AlgoPuzzleVQA(DatasetWrapper):
    def __init__(self, data_dir: str, img_dir: str = "data",
                 prompt_name: str = "cot_multi_extract",
                 prevent_direct_answer: bool = True,
                 use_describe_image_prompt: bool = True):
        # Static information

        # The root folder of the dataset
        self.root_folder = "data/LLM-PuzzleTest/AlgoPuzzleVQA"

        # The folder relative to the root folder containing the input
        # and the output
        self.root_data = "data"
        self.output_dir = "outputs"

        # Folder within the data folder containing the specific type of data
        # to be used
        self.data_dir = data_dir


        # Output file
        self.path_out = f"{self.root_folder}/{self.root_data}/{self.data_dir}"\
            "/{model_name}/{prompt_name}.jsonl"

        self.data = Data.load_with_image_dir(self.type_data, img_dir)
        # model_name = kwargs.get("model_name")

        self.resizer = EvalModel()

        self.progress = tqdm(self.data.samples, desc=self.path_out)
        self.prompter = select_prompter(prompt_name)

        # Variable to be set to the prompter when model name is known
        self.prevent_direct_answer = prevent_direct_answer
        self.use_describe_image_prompt = use_describe_image_prompt


        # Contains all the data
        self.progress = None

        # # List of booleans determining whether it was correctly answered or not
        # self.is_correct = []

    def set_model(self, model_name):
        """
        Set additional settings based on the used model.
        """
        self.set_prompter(model_name)

    def set_prompter(self, model_name):
        """
        Set settings of the prompter based on the used model.
        """
        # GPT-4V sometimes becomes very lazy when prompted not to directly
        # give the final answer
        prevent_direct_answer = self.prevent_direct_answer and \
            "openai" not in model_name and \
            "llava"  not in model_name and \
            "claude" not in model_name

        self.prompter.base.prompter.prevent_direct_answer = prevent_direct_answer

        self.prompter.base_prompter.use_describe_image_prompt = self.use_describe_image_prompt

    def evaluate(self):
        for sample in self.progress:
            # Initial zero-shot prompting
            sample.prompt = self.prompter.base_prompter.run(sample)
            image = convert_text_to_image(sample.image_string)
            image_data = convert_image_to_text(
                self.resizer.resize_image(image))
            image_url = convert_image_to_text(image)
            yield sample.prompt, image_data, image_url
