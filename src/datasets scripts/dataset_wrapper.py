"""
Template for dataset wrapper to be able to select a model to evaluate
the dataset.
"""


class DatasetWrapper:
    def __init__(self):
        # The root folder of the dataset
        self.root_folder = None

    def evaluate(self, model):
        ...
