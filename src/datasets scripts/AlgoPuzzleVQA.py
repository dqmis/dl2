"""
Dataset wrapper for AlgoPuzzleVQA, adapted from its main.py file.
"""

from pydantic import BaseModel
from tqdm import tqdm
from PIL import Image
from typing import Optional, List

from dataset_wrapper import DatasetWrapper

from data.LLM_PuzzleTest.AlgoPuzzleVQA.data_loading import (
    Data, Sample, convert_text_to_image, convert_image_to_text)
from data.LLM_PuzzleTest.AlgoPuzzleVQA.modeling import select_model
from data.LLM_PuzzleTest.AlgoPuzzleVQA.prompting import select_prompter


class Scorer(BaseModel):
    def run(self, sample: Sample) -> float:
        raise NotImplementedError


class ExactScorer(Scorer):
    def run(self, sample: Sample) -> float:
        if sample.pred == sample.answer:
            return 1.0
        return 0.0


class AlgoPuzzleVQA(DatasetWrapper):
    def __init__(self, data_dir: str, img_dir: str = "data",
                 prompt_name: str = "cot_multi_extract",
                 prevent_direct_answer: bool = True,
                 use_describe_image_prompt: bool = True,
                 **kwargs):
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

        # Type of scorer
        self.scorer = ExactScorer()

        # Output file
        self.path_out = f"{self.root_folder}/{self.root_data}/{self.data_dir}"\
            "/{model_name}/{prompt_name}.jsonl"

        self.data = Data.load_with_image_dir(self.type_data, img_dir)
        # model_name = kwargs.get("model_name")

        self.progress = tqdm(self.data.samples, desc=self.path_out)
        self.prompter = select_prompter(prompt_name)
        self.model = select_model(**kwargs)  # TODO: replace by Logic-LM
        self.set_model(prevent_direct_answer,
                       use_describe_image_prompt)

        # Information updated per iteration

        # Contains all the data
        self.progress = None

        # List of booleans determining whether it was correctly answered or not
        self.is_correct = []

    # TODO: check if still needed
    # def set_model(self,
    #               prevent_direct_answer: bool = True,
    #               use_describe_image_prompt: bool = True):
    #     # GPT-4V sometimes becomes very lazy when prompted not to directly
    #     # give the final answer
    #     if (
    #         "openai" in self.model.model_path
    #         or "llava" in self.model.model_path
    #         or "claude" in self.model.model_path
    #         or not prevent_direct_answer
    #     ):
    #         self.prompter.base_prompter.prevent_direct_answer = False

    #     if not use_describe_image_prompt:
    #         self.prompter.base_prompter.use_describe_image_prompt = False

    def evaluate(self):
        for sample in self.progress:
            # Initial zero-shot prompting
            sample.prompt = self.prompter.base_prompter.run(sample)
            image = convert_text_to_image(sample.image_string)
            yield sample.prompt, image, None

            # TODO: check if still needed
            # sample.raw_output = model.run(sample.prompt, image)
            # sample.pred = self.prompter.get_answer(
            #     sample.raw_output, sample.options)

            # # Model-based extraction if prediction not valid
            # if sample.pred not in sample.options:
            #     sample.prompt = self.prompter.run(sample)
            #     sample.raw_output = model.run(sample.prompt, image)
            #     sample.pred = self.prompter.get_answer(
            #         sample.raw_output, sample.options)

            # # Scoring
            # self.is_correct.append(self.scorer.run(sample))
            # score = sum(self.is_correct) / len(self.is_correct)
            # self.progress.set_postfix(score=score)
            # print(sample.json(indent=2, exclude={"image_string"}))
            # print(dict(is_correct=self.is_correct[-1]))
            # self.data.save(self.path_out)
