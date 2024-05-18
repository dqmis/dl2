import os
from PIL import Image

from dataset_wrapper import DatasetWrapper

from LLM_PuzzleTest.AlgoPuzzleVQA.data_loading import convert_image_to_text

class GameSET(DatasetWrapper):
    def __init__(self):
        # TODO: move the SET folder to this directory
        self.root_folder = "SET"
        self.root_data_dir = "data"
        self.output_dir = "outputs"
        self.images_folder = "images"
        self.text_folder = "text"
        self.asp_folder = "asp"

        self.image_files = self.find_files(self.images_folder)
        self.text_files = self.find_files(self.text_folder)
        self.asp_files = self.find_files(self.asp_folder)

    def find_files(self, subfolder):
        files = []
        for file in os.listdir(f"{self.root_folder}/{self.root_data_dir}/{subfolder}"):
            file = f"{self.root_folder}/{self.root_data_dir}/{self.images_folder}/{file}"
            files.append(file)

        return files

    def load_data(self, file, is_image=False):
        with open(file, mode='r', encoding='utf-8') as f:
            data = f.readlines()

        if is_image:
            data = Image.open(data)
            data = convert_image_to_text(data)

        return data


    def evaluate(self, use_images=False):
        if use_images:
            prompt = "Analyze the provided image of a SET game layout. Identify all sets, where a set consists of three cards with each attribute (shape, color, number, shading) either all the same or all different. List each set by describing the attributes of the three cards. Response Example: 'Set 1: [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]' Set 2: ... If no sets are found, state 'No sets found'."

            for i in range(len(self.image_files)):
                image_data = self.load_data(self.image_files[i], is_image=True)
                yield prompt, image_data, None

        prompt = "Analyze the provided text of a SET game layout. Identify all sets, where a set consists of three cards with each attribute (shape, color, number, shading) either all the same or all different. List each set by describing the attributes of the three cards. Response Example: 'Set 1: [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]' Set 2: ... If no sets are found, state 'No sets found'."

        for i in range(len(self.text_files)):
            text = self.load_data(self.text_files[i])
            yield f"{prompt} {text}", None, None
