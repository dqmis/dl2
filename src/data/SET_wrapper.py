import os

from dataset_wrapper import DatasetWrapper

class GameSET(DatasetWrapper):
    def __init__(self):
        # TODO: move the SET folder to this directory
        self.root_folder = "SET"
        self.root_data_dir = "data"
        self.output_dir = "outputs"
        self.images_folder = "images"
        self.text_folder = "text"
        self.asp_folder = "asp"

        self.image_data = self.load_files(self.images_folder)
        self.text_data = self.load_files(self.text_folder)
        self.asp_data = self.load_files(self.asp_folder)

    def load_files(self, subfolder):
        files = []
        for file in os.listdir(f"{self.root_folder}/{self.root_data_dir}/{subfolder}"):
            file = f"{self.root_folder}/{self.root_data_dir}/{self.images_folder}/{file}"
            files.append(file)

        return files


    def evaluate(self, use_images=False):
        prompt = "Analyze the provided image of a SET game layout. Identify all sets, where a set consists of three cards with each attribute (shape, color, number, shading) either all the same or all different. List each set by describing the attributes of the three cards. Response Example: 'Set 1: [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]; [Number], [Color], [Shading], [Shape]' Set 2: ... If no sets are found, state 'No sets found'."
