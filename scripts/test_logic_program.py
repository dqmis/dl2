
import transformers
import torch
from huggingface_hub import login
torch.cuda.empty_cache()


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
file_path = "/home/scur0401/DL2/dl2/Logic-LLM/data/AR-LSAT/dev.json"

with open(file_path, 'r') as json_file:
    
    data = json.load(json_file)

messages = []
for index in range(len(data)):
    message = []
    logic_program_prompts = """
    Given a problem description and a question. The task is to formulate the problem as a logic program, consisting three parts: Declarations, Constraints, and Options.
Declarations: Declare the variables and functions.
Constraints: Write the constraints in the problem description as logic formulas.
Options: Write the options in the question as logic formulas.
------
Problem:
On Tuesday Vladimir and Wendy each eat exactly four separate meals: breakfast, lunch, dinner, and a snack. The following is all that is known about what they eat during that day: At no meal does Vladimir eat the same kind of food as Wendy. Neither of them eats the same kind of food more than once during the day. For breakfast, each eats exactly one of the following: hot cakes, poached eggs, or omelet. For lunch, each eats exactly one of the following: fish, hot cakes, macaroni, or omelet. For dinner, each eats exactly one of the following: fish, hot cakes, macaroni, or omelet. For a snack, each eats exactly one of the following: fish or omelet. Wendy eats an omelet for lunch.
Question:
Vladimir must eat which one of the following foods?
Choices:
(A) fish
(B) hot cakes
(C) macaroni
(D) omelet
(E) poached eggs
###
# Declarations
people = EnumSort([Vladimir, Wendy])
meals = EnumSort([breakfast, lunch, dinner, snack])
foods = EnumSort([fish, hot_cakes, macaroni, omelet, poached_eggs])
eats = Function([people, meals] -> [foods])

# Constraints
ForAll([m:meals], eats(Vladimir, m) != eats(Wendy, m)) ::: At no meal does Vladimir eat the same kind of food as Wendy
ForAll([p:people, f:foods], Count([m:meals], eats(p, m) == f) <= 1) ::: Neither of them eats the same kind of food more than once during the day
ForAll([p:people], Or(eats(p, breakfast) == hot_cakes, eats(p, breakfast) == poached_eggs, eats(p, breakfast) == omelet)) ::: For breakfast, each eats exactly one of the following: hot cakes, poached eggs, or omelet
ForAll([p:people], Or(eats(p, lunch) == fish, eats(p, lunch) == hot_cakes, eats(p, lunch) == macaroni, eats(p, lunch) == omelet)) ::: For lunch, each eats exactly one of the following: fish, hot cakes, macaroni, or omelet
ForAll([p:people], Or(eats(p, dinner) == fish, eats(p, dinner) == hot_cakes, eats(p, dinner) == macaroni, eats(p, dinner) == omelet)) ::: For dinner, each eats exactly one of the following: fish, hot cakes, macaroni, or omelet
ForAll([p:people], Or(eats(p, snack) == fish, eats(p, snack) == omelet)) ::: For a snack, each eats exactly one of the following: fish or omelet
eats(Wendy, lunch) == omelet ::: Wendy eats an omelet for lunch

# Options
Question ::: Vladimir must eat which one of the following foods?
is_valid(Exists([m:meals], eats(Vladimir, m) == fish)) ::: (A)
is_valid(Exists([m:meals], eats(Vladimir, m) == hot_cakes)) ::: (B)
is_valid(Exists([m:meals], eats(Vladimir, m) == macaroni)) ::: (C)
is_valid(Exists([m:meals], eats(Vladimir, m) == omelet)) ::: (D)
is_valid(Exists([m:meals], eats(Vladimir, m) == poached_eggs)) ::: (E)
------
Problem:
In a repair facility there are exactly six technicians: Stacy, Urma, Wim, Xena, Yolanda, and Zane. Each technician repairs machines of at least one of the following three types—radios, televisions, and VCRs—and no other types. The following conditions apply: Xena and exactly three other technicians repair radios. Yolanda repairs both televisions and VCRs. Stacy does not repair any type of machine that Yolanda repairs. Zane repairs more types of machines than Yolanda repairs. Wim does not repair any type of machine that Stacy repairs. Urma repairs exactly two types of machines.
Question:
Which one of the following pairs of technicians could repair all and only the same types of machines as each other?
Choices:
(A) Stacy and Urma
(B) Urma and Yolanda
(C) Urma and Xena
(D) Wim and Xena
(E) Xena and Yolanda
###
# Declarations
technicians = EnumSort([Stacy, Urma, Wim, Xena, Yolanda, Zane])
machines = EnumSort([radios, televisions, VCRs])
repairs = Function([technicians, machines] -> [bool])

# Constraints
ForAll([t:technicians], Count([m:machines], repairs(t, m)) >= 1) ::: each technician repairs machines of at least one of the following three types
And(repairs(Xena, radios), Count([t:technicians], And(t != Xena, repairs(t, radios))) == 3) ::: Xena and exactly three other technicians repair radios
And(repairs(Yolanda, televisions), repairs(Yolanda, VCRs)) ::: Yolanda repairs both televisions and VCRs
ForAll([m:machines], Implies(repairs(Yolanda, m), Not(repairs(Stacy, m)))) ::: Stacy does not repair any type of machine that Yolanda repairs
Count([m:machines], repairs(Zane, m)) > Count([m:machines], repairs(Yolanda, m)) ::: Zane repairs more types of machines than Yolanda repairs
ForAll([m:machines], Implies(repairs(Stacy, m), Not(repairs(Wim, m)))) ::: Wim does not repair any type of machine that Stacy repairs
Count([m:machines], repairs(Urma, m)) == 2 ::: Urma repairs exactly two types of machines

# Options
Question ::: ::: Which one of the following pairs of technicians could repair all and only the same types of machines as each other?
is_sat(ForAll([m:machines], repairs(Stacy, m) == repairs(Urma, m))) ::: (A)
is_sat(ForAll([m:machines], repairs(Urma, m) == repairs(Yolanda, m))) ::: (B)
is_sat(ForAll([m:machines], repairs(Urma, m) == repairs(Xena, m))) ::: (C)
is_sat(ForAll([m:machines], repairs(Wim, m) == repairs(Xena, m))) ::: (D)
is_sat(ForAll([m:machines], repairs(Xena, m) == repairs(Yolanda, m))) ::: (E)
------
Problem:
Workers at a water treatment plant open eight valves—G, H, I, K, L, N, O, and P—to flush out a system of pipes that needs emergency repairs. To maximize safety and efficiency, each valve is opened exactly once, and no two valves are opened at the same time. The valves are opened in accordance with the following conditions: Both K and P are opened before H. O is opened before L but after H. L is opened after G. N is opened before H. I is opened after K.
Question: Each of the following could be the fifth valve opened EXCEPT:
Choices:
(A) H
(B) I
(C) K
(D) N
(E) O

# Declarations
valves = EnumSort([G, H, I, K, L, N, O, P])
opened = Function([valves] -> [int])
ForAll([v:valves], And(1 <= opened(v), opened(v) <= 8))

# Constraints
Distinct([v:valves], opened(v)) ::: no two valves are opened at the same time
And(opened(K) < opened(H), opened(P) < opened(H)) ::: Both K and P are opened before H
And(opened(O) > opened(H), opened(O) < opened(L)) ::: O is opened before L but after H
opened(L) > opened(G) ::: L is opened after G
opened(N) < opened(H) ::: N is opened before H
opened(I) > opened(K) ::: I is opened after K

# Options
Question ::: Each of the following could be the fifth valve opened EXCEPT:
is_exception(is_sat(opened(H) == 5)) ::: (A)
is_exception(is_sat(opened(I) == 5)) ::: (B)
is_exception(is_sat(opened(K) == 5)) ::: (C)
is_exception(is_sat(opened(N) == 5)) ::: (D)
is_exception(is_sat(opened(O) == 5)) ::: (E)
------
"""

    message.append({"role": "system", "content": logic_program_prompts})
    #content = data[index]['context'] +' ' + data[index]['question']+' '
    #content += ' '.join(data[index]['options'])
    d = {}
    d["role"] = "user"
    d["content"] = "Problem: \n"+data[index]['context']+"\n"+"Question: \n"+data[index]['question']+"\n"+"Choices:\n"+'\n'.join(data[index]['options'])+"\n" 
   
    
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
