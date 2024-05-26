# Installing
Install the Python packages using the [requirements file](Logic-LLM/requirements.txt), adapted from the original [Logic-LM repository](https://github.com/teacherpeterpan/Logic-LLM).

NOTE: Logic-LLM/evaluation_gemini.sh and logic_inference_gemini.sh use environment solver2, but logic_programs_gemini.sh mentions DL2.
TODO: explain what the environment name should be

# LLMs
For this project various Large Language Models (LLMs) are used, namely GPT-4, Gemini and LLaMA. For GPT-4, an API key is required to run the code. To work with Gemini models, we utilized Vertex AI. Finally, LLaMA is accessed with Hugging Face, of which a login is needed.

TODO: maybe better explanation

# How to use
The [commands](https://github.com/teacherpeterpan/Logic-LLM/blob/main/README.md) mentioned in the original repository are still available. Additionally, shell scripts are added in the Logic-LLM folder to support Gemini models. Furthermore, Python scripts are added in the root folder for testing various components, including the support of LLaMA models, by using one example as input.

TODO: explain which shell scripts when to use
