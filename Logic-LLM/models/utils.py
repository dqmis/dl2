import asyncio
import base64
import io
import os
import time
from time import sleep
from typing import Any, Optional

import model_globals
import openai
import vertexai
from google.api_core.exceptions import ResourceExhausted
from google.oauth2 import service_account
from openai import AzureOpenAI
from PIL import Image as PILImage
from vertexai.generative_models import GenerationConfig, GenerativeModel
from vertexai.generative_models import Image as VertexAIImage
from vertexai.generative_models import Part


# @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


# @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def load_image(image_path):
    image = VertexAIImage.load_from_file(image_path)
    return Part.from_image(image)


def load_gpt_image(image_path):
    image = PILImage.open(image_path)
    return image


class GPTRunner:
    def __init__(self):
        api_base = os.environ.get("API_BASE", "https://api.openai.com")
        api_key = os.environ.get("API_KEY")
        deployment_name = "gpt4"
        api_version = "2023-12-01-preview"

        self.client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            base_url=f"{api_base}/openai/deployments/{deployment_name}",
        )
        self.deployment_name = deployment_name

    def _image_to_base64(self, image: PILImage.Image):
        image_bytes = io.BytesIO()
        image.save(image_bytes, format=image.format)
        return base64.b64encode(image_bytes.getvalue()).decode("utf-8")

    def generate(self, inputs: Any) -> str:
        if isinstance(inputs, tuple):
            # fist element is prompt, all the rest are images
            prompt, images = inputs[0], inputs[1:]
            images = list(images)
        else:
            prompt, images = inputs, None

        return self._generate(prompt, images)

    def _generate(self, prompt: str, images: list[PILImage.Image] = None):
        images = (
            [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{self._image_to_base64(image)}",
                        "detail": "high",
                    },
                }
                for image in images
            ]
            if images
            else []
        )

        messages = [
            {"role": "user", "content": [{"type": "text", "text": prompt}] + images}
        ]
        backoff = 20
        while True:
            try:
                response = self.client.chat.completions.create(
                    model=self.deployment_name,
                    messages=messages,
                    max_tokens=2024,
                    temperature=0.0,
                    n=1,
                )
                return response.choices[0].message.content
            except Exception as e:
                print("Got an error:", e)
                print("Retrying in", backoff, "seconds")
                sleep(backoff)
                backoff *= 2


async def dispatch_openai_chat_requests(
    messages_list: list[list[dict[str, Any]]],
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    stop_words: list[str],
) -> list[str]:
    """Dispatches requests to OpenAI API asynchronously.

    Args:
        messages_list: List of messages to be sent to OpenAI ChatCompletion API.
        model: OpenAI model to use.
        temperature: Temperature to use for the model.
        max_tokens: Maximum number of tokens to generate.
        top_p: Top p to use for the model.
        stop_words: List of words to stop the model from generating.
    Returns:
        List of responses from OpenAI API.
    """
    async_responses = [
        openai.ChatCompletion.acreate(
            model=model,
            messages=x,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stop=stop_words,
        )
        for x in messages_list
    ]
    return await asyncio.gather(*async_responses)


async def dispatch_openai_prompt_requests(
    messages_list: list[list[dict[str, Any]]],
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    stop_words: list[str],
) -> list[str]:
    async_responses = [
        openai.Completion.acreate(
            model=model,
            prompt=x,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=stop_words,
        )
        for x in messages_list
    ]
    return await asyncio.gather(*async_responses)


class OpenAIModel:
    def __init__(self, API_KEY, model_name, stop_words, max_new_tokens) -> None:
        openai.api_key = API_KEY
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.stop_words = stop_words

    # used for chat-gpt and gpt-4
    def chat_generate(self, input_string, temperature=0.0):
        response = chat_completions_with_backoff(
            model=self.model_name,
            messages=[{"role": "user", "content": input_string}],
            max_tokens=self.max_new_tokens,
            temperature=temperature,
            top_p=1.0,
            stop=self.stop_words,
        )
        generated_text = response["choices"][0]["message"]["content"].strip()
        return generated_text

    # used for text/code-davinci
    def prompt_generate(self, input_string, temperature=0.0):
        response = completions_with_backoff(
            model=self.model_name,
            prompt=input_string,
            max_tokens=self.max_new_tokens,
            temperature=temperature,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=self.stop_words,
        )
        generated_text = response["choices"][0]["text"].strip()
        return generated_text

    def generate(self, input_string, temperature=0.0):
        if self.model_name in [
            "text-davinci-002",
            "code-davinci-002",
            "text-davinci-003",
        ]:
            return self.prompt_generate(input_string, temperature)
        elif self.model_name in ["gpt-4", "gpt-3.5-turbo"]:
            return self.chat_generate(input_string, temperature)
        else:
            raise Exception("Model name not recognized")

    def batch_chat_generate(self, messages_list, temperature=0.0):
        open_ai_messages_list = []
        for message in messages_list:
            open_ai_messages_list.append([{"role": "user", "content": message}])
        predictions = asyncio.run(
            dispatch_openai_chat_requests(
                open_ai_messages_list,
                self.model_name,
                temperature,
                self.max_new_tokens,
                1.0,
                self.stop_words,
            )
        )
        return [x["choices"][0]["message"]["content"].strip() for x in predictions]

    def batch_prompt_generate(self, prompt_list, temperature=0.0):
        predictions = asyncio.run(
            dispatch_openai_prompt_requests(
                prompt_list,
                self.model_name,
                temperature,
                self.max_new_tokens,
                1.0,
                self.stop_words,
            )
        )
        return [x["choices"][0]["text"].strip() for x in predictions]

    def batch_generate(self, messages_list, temperature=0.0):
        if self.model_name in [
            "text-davinci-002",
            "code-davinci-002",
            "text-davinci-003",
        ]:
            return self.batch_prompt_generate(messages_list, temperature)
        elif self.model_name in ["gpt-4", "gpt-3.5-turbo"]:
            return self.batch_chat_generate(messages_list, temperature)
        else:
            raise Exception("Model name not recognized")

    def generate_insertion(self, input_string, suffix, temperature=0.0):
        response = completions_with_backoff(
            model=self.model_name,
            prompt=input_string,
            suffix=suffix,
            temperature=temperature,
            max_tokens=self.max_new_tokens,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        generated_text = response["choices"][0]["text"].strip()
        return generated_text


class GenimiModel:
    def __init__(self, model_name, stop_words, max_new_tokens) -> None:
        self.model_name = model_name
        self.stop_sequences = stop_words[:5]
        credentials = service_account.Credentials.from_service_account_file("key.json")
        vertexai.init(
            project="sunny-mender-423218-i9",
            credentials=credentials,
        )

        generation_config = GenerationConfig(
            temperature=0.0, top_p=1.0, max_output_tokens=2048
        )
        self.LLM = GenerativeModel(
            model_name=self.model_name, generation_config=generation_config
        )

    def gemini_generate(
        self,
        input_string,
        images: Optional[list] = None,
        max_retries=10,
        max_wait_time=120,
    ):
        start_time = time.time()
        retry_count = 0
        backoff_factor = 1

        if type(input_string) is tuple:
            input = list(input_string)
        else:
            input = [input_string]

        while retry_count < max_retries and (time.time() - start_time) < max_wait_time:
            try:
                chat = self.LLM.start_chat(history=[])
                response = chat.send_message(input)
                generated_text = response.text
                return generated_text
            except ResourceExhausted:
                print(f"Rate limited, retrying in {backoff_factor} seconds...")
                time.sleep(backoff_factor)
                backoff_factor *= 2  # Exponential backoff
                retry_count += 1

        raise Exception("Failed after multiple retries or maximum wait time exceeded")

    def generate(self, input_string):
        if self.model_name in model_globals.GEMINI_MODEL_NAMES:
            return self.gemini_generate(input_string)
        else:
            raise Exception("Model name not recognized")

    async def dispatch_gemini_requests(self, input_string) -> str:
        print(input_string[0])
        if type(input_string) is tuple:
            input = list(input_string)
        else:
            input = [input_string]
        r = await self.LLM.generate_content_async(input)
        return r.text

    async def batch_gemini_generate(self, input_strings):
        jobs = asyncio.gather(
            *[
                self.dispatch_gemini_requests(input_string)
                for input_string in input_strings
            ]
        )
        results = await jobs
        return results

    def batch_generate(self, input_strings):
        if self.model_name in model_globals.GEMINI_MODEL_NAMES:
            return self.batch_gemini_generate(input_strings)
        else:
            raise Exception("Model name not recognized")
