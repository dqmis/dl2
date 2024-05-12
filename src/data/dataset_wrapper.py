"""
Template for dataset wrapper to be able to select a model to evaluate
the dataset.
"""


class DatasetWrapper:
    def __init__(self):
        # The root folder of the dataset
        self.root_folder = None
        self.data = []

    def set_model(self, model_name):
        """
        Set additional settings once the model is known.
        """
        pass

    def evaluate(self):
        """
        For-loop over examples in data.

        Per data point, yields the prompt, image_data and image_url.
        """

        # Template
        for i in range(len(self.data)):
            prompt = ""

            # When using an image, set these values, which one is used depends
            # on LLM
            image_data = None  # for AlgoPuzzleVQA dataset
            image_url = None  # for Rebus dataset

            # TODO: maybe improve, it needs some generic return values,
            # so it can be used for 'every' LLM (GPT, Gemini, Llama, etc).
            # Certain functions from the dataset scripts, such as
            # 'convert_image_to_text' or 'make_messages' are LLM-dependent and
            # can be handled through the LLM class instead of these
            # dataset classes
            yield prompt, image_data, image_url

        # inputs.append({"type": "image_url", "image_url": {"url": url}})

        # return [{"role": "user", "content": inputs}]
