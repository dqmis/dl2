"""
Template for dataset wrapper to be able to select a model to evaluate
the dataset.
"""


class DatasetWrapper:
    def __init__(self):
        # The root folder of the dataset
        self.root_folder = None
        self.data = []

    def evaluate(self):
        """
        For-loop over examples in data. Yields the 'messages' list, which
        includes the prompt, to give to an LLM.
        """

        # Template
        for i in range(len(self.data)):
            prompt = ""

            # When using an image, either give the encoding or give the url.
            # Set the other value to None.
            image_string = None  # for AlgoPuzzleVQA dataset
            image_url = None  # for Rebus dataset

            # TODO: maybe improve, it needs some generic return values,
            # so it can be used for 'every' LLM (GPT, Gemini, Llama, etc).
            # Certain functions from the dataset scripts, such as
            # 'convert_image_to_text' or 'make_messages' are LLM-dependent and
            # can be handled through the LLM class instead of these
            # dataset classes
            yield prompt, image_string, image_url
