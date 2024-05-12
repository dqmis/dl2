"""
This file is used for testing purposes
"""
import base64
import requests

from AlgoPuzzleVQA import AlgoPuzzleVQA
from MathVision import MathVision
from rebus import Rebus


def create_message_gpt4_vision(prompt, image_data, image_url):
    inputs = [{"type": "text", "text": prompt}]

    if image_url is not None:
        image_url = f"data:image/jpeg;base64,{image_data}"

    inputs.append({"type": "image_url", "image_url": {"url": image_url}})
    return inputs


def create_message_gemini_vision(prompt, image_data, image_url):
    if image_url is not None:
        # TODO: for the Rebus dataset, a request is send to the website API of Gemini,
        # not sure how to handle this as a message with the Python class
        image_data = requests.get(image_url).content

        image = base64.b64encode(image_data).decode("utf-8")
        return

    if image_data is not None:
        return [prompt, image_data]

    return prompt


def send_message(model_name, prompt, image_data, image_url):
    if model_name == "gpt-4-vision-preview":
        msg = create_message_gpt4_vision(prompt, image_data, image_url)

        # NOTE: Use 'openai.ChatCompletions' for older version, like the openai version used for Logic-LM
        # response = client.chat.completions.create(
        #     model=self.engine,
        #     messages=msg,
        #     temperature=self.temperature,
        #     max_tokens=512,
        # )
        return msg

    if "gemini" in model_name and "vision" in model_name:  # TODO: find correct names
        msg = create_message_gemini_vision(prompt, image_data, image_url)

        # NOTE: Used for datasets AlgoPuzzleVQA and MathVision
        # model = genai.GenerativeModel(model)

        # response = model.generate_content(
        #     messages,
        #     generation_config=genai.types.GenerationConfig(
        #         max_output_tokens=max_tokens,
        #         temperature=temperature,
        #         candidate_count=candidate_count,
        #         stop_sequences=stop_sequences
        #     ),
        #     # safety_settings=safety_settings
        # )

        # TODO: convert to code using vertex AI

        return msg


a = AlgoPuzzleVQA()
b = MathVision()
c = Rebus()

for dataset_wrapper in [a, b, c]:
    for model_name in ["gpt-4-vision-preview", "gemini-vision"]:
        dataset_wrapper.set_model(model_name)

        for prompt, image_data, image_url in a.evaluate():
            msg = send_message(model_name, prompt, image_data, image_url)
            print(msg)

        print()
