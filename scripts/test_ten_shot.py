
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
    extra_ten_samples = """
Problem: Exactly six trade representatives negotiate a treaty: Klosnik, Londi, Manley, Neri, Osata, Poirier. There are exactly six chairs evenly spaced around a circular table. The chairs are numbered 1 through 6, with successively numbered chairs next to each other and chair number 1 next to chair number 6. Each chair is occupied by exactly one of the representatives. The following conditions apply: Poirier sits immediately next to Neri. Londi sits immediately next to Manley, Neri, or both. Klosnik does not sit immediately next to Manley. If Osata sits immediately next to Poirier, Osata does not sit immediately next to Manley.
Question: Which one of the following seating arrangements of the six representatives in chairs 1 through 6 would NOT violate the stated conditions?\
options: 
A) Klosnik, Poirier, Neri, Manley, Osata, Londi
B) Klosnik, Londi, Manley, Poirier, Neri, Osata
C) Klosnik, Londi, Manley, Osata, Poirier, Neri
D) Klosnik, Osata, Poirier, Neri, Londi, Manley
E) Klosnik, Neri, Londi, Osata, Manley, Poirier
Correct Answer: B

Problem: A small software firm has four offices, numbered 1, 2, 3, and 4. Each of its offices has exactly one computer and exactly one printer. Each of these eight machines was bought in either 1987, 1988, or 1989. The eight machines were bought in a manner consistent with the following conditions: The computer in each office was bought either in an earlier year than or in the same year as the printer in that office. The computer in office 2 and the printer in office 1 were bought in the same year. The computer in office 3 and the printer in office 4 were bought in the same year. The computer in office 2 and the computer in office 3 were bought in different years. The computer in office 1 and the printer in office 3 were bought in 1988.
Question: If the computer in office 4 was bought in 1988, then which one of the following statements must be true?
options: 
A) The printer in office 1 was bought in 1988.
B) The printer in office 1 was bought in 1989.
C) The computer in office 2 was bought in 1988.
D) The computer in office 3 was bought in 1987.
E) The printer in office 4 was bought in 1989.
Correct Answer: B

Problem: Arbutus College owns exactly four houses that it leases to faculty or students. Of these houses, no two are exactly the same distance from Arbutus's campus, and each house is either a student house (occupied entirely by students) or a faculty house (occupied entirely by faculty). The lease length for each house is one, two, or three semesters. The following conditions must hold: No student house has a three-semester lease. At least two houses each have longer leases than does the house closest to campus. Every student house (if there are any) is farther from campus than any faculty house (if there are any).
Question: What is the maximum number of houses that could all be student houses with two-semester leases?
options:
A) zero
B) one
C) two
D) three
E) four
Correct Answer: D

Problem: Meena has six colored pencils—green, maroon, orange, red, white, and yellow. She sketches a drawing using exactly five of the six pencils, one pencil at a time. The following conditions must hold: No pencil is used more than once. Either the maroon or the yellow pencil is not used. The red pencil is used at some time before the green. The red pencil is used at some time before either the orange or the yellow, but not before both. The green pencil is used at some time before either the maroon or the white, but not before both.
Question: Which one of the following could be an accurate list of the pencils used, from first to fifth?
options:
A) orange, green, red, maroon, yellow
B) red, green, orange, white, maroon
C) red, orange, maroon, white, green
D) white, red, orange, green, maroon
E) white, yellow, orange, green, red
Correct Answer: D

Problem: A six-week literature course is being planned in which six books—F, K, N, O, R, and T—will be discussed. The books will be discussed one at a time, one book per week. In addition, written summaries will be required for one or more of the books. The order in which the books are discussed and the selection of books to be summarized is subject to the following conditions: No two books that are summarized are discussed in consecutive weeks. If N is not summarized, then both R and T are summarized. N is discussed earlier than T, and T is discussed earlier than O. F is discussed earlier than O, and O is discussed earlier than both K and R.
Question: Which one of the following could be the plan for the course, showing the order, from first to last, in which the books are discussed and the choice of books to be summarized?
options:
A) F, N, T, O, R, K; with only T and R summarized
B) F, T, N, O, K, R; with only N and K summarized
C) N, F, T, O, K, R; with only T, O, and R summarized
D) N, T, F, O, K, R; with only T and O summarized
E) N, T, O, F, K, R; with only T and R summarized
Correct Answer: A

Problem: Three couples—John and Kate, Lewis and Marie, and Nat and Olive have dinner in a restaurant together. Kate, Marie, and Olive are women; the other three are men. Each person orders one and only one of the following kinds of entrees: pork chops, roast beef, swordfish, tilefish, veal cutlet. The six people order in a manner consistent with the following conditions: The two people in each couple do not order the same kind of entree as each other. None of the men orders the same kind of entree as any of the other men. Marie orders swordfish. Neither John nor Nat orders a fish entree. Olive orders roast beef.
Question: Which one of the following statements must be true?
options:
A) One of the men orders pork chops or veal cutlet.
B) One of the men orders swordfish or veal cutlet.
C) Two of the women order tilefish.
D) None of the men orders a fish entree.
E) Exactly one of the women orders a fish entree.
Correct Answer: A

Problem: Hannah spends 14 days, exclusive of travel time, in a total of six cities. Each city she visits is in one of three countries—X, Y, or Z. Each of the three countries has many cities. Hannah visits at least one city in each of the three countries. She spends at least two days in each city she visits. She spends only whole days in any city.
Question: If Hannah visits a combined total of four cities in countries X and Y, what is the greatest total number of days she can spend visiting cities in country Y?
options:
A) 6
B) 7
C) 8
D) 9
E) 10
Correct Answer: C

Problem: There are exactly seven houses on a street. Each house is occupied by exactly one of seven families: the Kahns, Lowes, Muirs, Newmans, Owens, Piatts, Rutans. All the houses are on the same side of the street, which runs from west to east. The Rutans do not live in the first or the last house on the street. The Kahns live in the fourth house from the west end of the street. The Muirs live next to the Kahns. The Piatts live east of both the Kahns and the Muirs but west of the Lowes.
Question: If the Owens live east of the Kahns, which one of the following pairs of families must live next to each other?
options:
A) the Kahns and the Piatts
B) the Lowes and the Owens
C) the Muirs and the Newmans
D) the Newmans and the Rutans
E) the Owens and the Piatts
Correct Answer: D

Problem: Planes 1, 2, 3, and 4—and no others—are available to fly in an air show. Pilots Anna, Bob, and Cindy are all aboard planes that are flying in the show and they are the only qualified pilots in the show. Copilots Dave, Ed, and Fran are all aboard planes that are flying in the show and they are the only qualified copilots in the show. No plane flies in the show without a qualified pilot aboard. No one but qualified pilots and qualified copilots flies in the show. Anna will only fly in either plane 1 or plane 4. Dave will only fly in either plane 2 or plane 3.
Question: If plane 1 is used, its crew could consist of
options:
A) Anna, Bob, Cindy, Fran
B) Anna, Bob, Ed, Fran
C) Bob, Cindy, Ed, Fran
D) Bob, Cindy, Dave, Ed
E) Bob, Dave, Ed, Fran
Correct Answer: B

Problem: The Mammoth Corporation has just completed hiring nine new workers: Brandt, Calva, Duvall, Eberle, Fu, Garcia, Haga, Irving, and Jessup. Fu and Irving were hired on the same day as each other, and no one else was hired that day. Calva and Garcia were hired on the same day as each other, and no one else was hired that day. On each of the other days of hiring, exactly one worker was hired. Eberle was hired before Brandt. Haga was hired before Duvall. Duvall was hired after Irving but before Eberle. Garcia was hired after both Jessup and Brandt. Brandt was hired before Jessup.
Question: Exactly how many workers were hired before Jessup?
options:
A) 6
B) 5
C) 4
D) 3
E) 2
Correct Answer: A
"""

    message.append({"role": "system", "content": """
    f"You are a problem solving chatbot who has to identify the constraints and output the correct option. Note that only option is correct and the rest wrong. Here are some sample\
    problems along with their correct answers:\n"""+extra_ten_samples})
    #content = data[index]['context'] +' ' + data[index]['question']+' '
    #content += ' '.join(data[index]['options'])
    d = {}
    d["role"] = "user"
    d["content"] = "Problem: \n"+data[index]['context']+"\n"+"Question: \n"+data[index]['question']+"\n"+"options:\n"+'\n'.join(data[index]['options'])+"\n" + "Correct Answer: ### FILL THIS WITH THE CORRECT ANSWER ###"
   
    
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
