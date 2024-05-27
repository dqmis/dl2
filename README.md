# Installing the environments
Depending on what you want to reproduce, multiple distinct environments may need to be created. To just run the symbolic solvers on the logic programs in the repo, you need to install the Python packages using the [requirements file](Logic-LLM/requirements.txt), adapted from the original [Logic-LM repository](https://github.com/teacherpeterpan/Logic-LLM). The name can be changed, but note that the relevant bash scripts will assume it to be called `solver2'. 
```
conda create --name solver2
conda activate solver2
pip install -r requirements.txt
```
To reproduce the prompting with Gemini you need to create a conda env and install the package needed for VertexAI. Note that due to conflicts in versions of dependencies this has to be a seperate env. The name can be changed, but note that the relevant bash scripts will assume it to be called `DL2'. 
```
conda create --name DL2
conda activate DL2
pip install google-cloud-aiplatform
```
TODO what envs for Llama and GPT-4? What about for generating the multimodal datasets?
# Setting up the LLMs
For this project various Large Language Models (LLMs) are used, namely GPT-4, Gemini and LLaMA. For GPT-4, an API key is required to run the code. To work with Gemini models, we utilized Vertex AI. Finally, LLaMA is accessed with Hugging Face, of which a login is needed.
## Vertex AI for Gemini
To run the prompts using Vertex AI, you need to set up an account and a service account. See also the [quickstart](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal). Make sure to change the credentials to your own in the config files ([baseline](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/model_globals.py) and [Logic-LM](https://github.com/dqmis/dl2/tree/master/Logic-LLM/models/model_globals.py)). Using your environment run `gcloud auth login` in the command line and follow the instructions in the pop up to login.
## Azure (?) for GPT-4 
TODO

## Snellius/own accelerator for Llama
TODO

# How to use
## Reproducing Gemini results
The [commands](https://github.com/teacherpeterpan/Logic-LLM/blob/main/README.md) mentioned in the original repository are still available. Additionally, shell scripts are added in the Logic-LLM folder to support Gemini models. For all the following bash files, uncomment the line that sets `gemini_model` to the model version of interest and comment the others. 
### Baseline
#### Prompting
Note that our [results](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/results/) from the prompting are already in the github repo. Note that these are only the results using `gemini-1.5-flash-preview-0514`. To rerun these prompts (and for other model versions), go to the [baseline folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/) and run the right bash file. This will run the prompts for all datasets from the paper with both the Direct and CoT mode.
```
cd Logic-LLM/baselines
./baselines_gemini.sh
```
#### Evaluation
To evaluate all Gemini baseline results, go (back) to the [baseline folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/) and run:
```
conda deactivate
conda activate solver2
python3 ./baselines/evaluation_save.py
```
This will save the evaluation of the results in [evaluation_baselines.json](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/evaluation/evaluation_baselines.json). If you reuse our results from prompting the baseline and have not run it for the other models version, expect some `No results available for ...` to be printed when running this. 
### Logic-LM
#### Prompting
Note that our [results](https://github.com/dqmis/dl2/tree/master/Logic-LLM/outputs/logic_programs) from the prompting are already in the github repo. To rerun these prompts, go to the [Logic-LLM folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/) and run the right bash file. This will run the prompts for all datasets from the paper.
```
./logic_programs_gemini.sh
```
#### Running symbolic solvers
Note that our [results](https://github.com/dqmis/dl2/tree/master/Logic-LLM/outputs/logic_inference) from running the solvers on our own results of the prompting are already in the github repo. To rerun the solvers, go to (or stay in) the [Logic-LLM folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/) and run the right bash file. Note that by default the backup stategy of using the CoT baseline anwer from `gemini-1.5-flash-preview-0514` will be used. To change this, set `--backup_LLM_result_path` differently in [logic_inference_gemini.sh](https://github.com/dqmis/dl2/tree/master/Logic-LLM/models/logic_inference_gemini.sh). This will run the symbolic solvers for all datasets from the paper:
```
./logic_inference_gemini.sh
```
#### Evaluation
To evaluate all Gemini Logic-LM results, in the [Logic-LLM folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/) run:
```
conda deactivate
conda activate solver2
python3 ./models/evaluation_save.py
```
This will save the evaluation of the results in [evaluation_baselines.json](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/evaluation/evaluation_baselines.json).
### Order bias
#### Prompting
Note that our [results](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/results/) from the order bias prompting are already in the github repo. To rerun these prompts, go to the [Logic-LLM folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines) and run the right bash file. This will run the prompts for all datasets from the paper.
```
./order_bias_gemini.sh
```
#### Evaluation
To evaluate our experiments to determine order bias in the Gemini models, go (back) to the [baseline folder](https://github.com/dqmis/dl2/tree/master/Logic-LLM/baselines/) and run:
```
./evaluation_order_bias_gemini.sh
```
This will print the respective evaluations of the accuracy for the case in which we make the right option always at the same position. 
### Multimodal
TODO or make a seperate second-level heading??

## Reproducing LLama results
Python scripts are added in the root folder for testing various components, including the support of LLaMA models, by using one example as input.

TODO