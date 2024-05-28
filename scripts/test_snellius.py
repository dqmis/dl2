
import transformers
import torch
from huggingface_hub import login

login("..")

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
#model_id = "meta-llama/Llama-2-7b-chat-hf"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)



# Direct prompting
import json
file_path = "/home/scur0401/DL2/dl2/Logic-LLM/data/AR-LSAT/test.json"

with open(file_path, 'r') as json_file:
    
    data = json.load(json_file)

messages = []
for index in range(len(data)):
    message = []
    message.append({"role": "system", "content": "You are a problem solving chatbot who always analzes the problem, formulates the constraints and selects all the wrong answer choices. Note that only 1 answer choice is correct and rest are wrong. You have to select all the wrong answer choices."})
    content = data[index]['context'] +' ' + data[index]['question']+' '
    content += ' '.join(data[index]['options'])
    d = {}
    d["role"] = "user"
    d["content"] = content
    message.append(d)
    messages.append(message)


for message in messages:


    prompt = pipeline.tokenizer.apply_chat_template(
            message, 
            tokenize=False, 
            add_generation_prompt=True
    )

    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
        prompt,
        max_new_tokens=1024,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    print("LLama3 Response begins:")
    print(outputs[0]["generated_text"][len(prompt):])
    print("LLama3 Response ends:")
