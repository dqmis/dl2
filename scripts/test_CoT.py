
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
file_path = "/home/scur0401/DL2/dl2/Logic-LLM/data/AR-LSAT/test.json"

with open(file_path, 'r') as json_file:
    
    data = json.load(json_file)

messages = []
for index in range(len(data)):
    message = []

cot_samples = """
Problem: Exactly six trade representatives negotiate a treaty: Klosnik, Londi, Manley, Neri, Osata, Poirier. There are exactly six chairs evenly spaced around a circular table. The chairs are numbered 1 through 6, with successively numbered chairs next to each other and chair number 1 next to chair number 6. Each chair is occupied by exactly one of the representatives. The following conditions apply: Poirier sits immediately next to Neri. Londi sits immediately next to Manley, Neri, or both. Klosnik does not sit immediately next to Manley. If Osata sits immediately next to Poirier, Osata does not sit immediately next to Manley.
Question: Which one of the following seating arrangements of the six representatives in chairs 1 through 6 would NOT violate the stated conditions?\
options: 
A) Klosnik, Poirier, Neri, Manley, Osata, Londi
B) Klosnik, Londi, Manley, Poirier, Neri, Osata
C) Klosnik, Londi, Manley, Osata, Poirier, Neri
D) Klosnik, Osata, Poirier, Neri, Londi, Manley
E) Klosnik, Neri, Londi, Osata, Manley, Poirier
Reasoning: Let's analyze the problem step by step by examining each option against the given conditions:

Condition 1: Poirier sits immediately next to Neri.
Condition 2: Londi sits immediately next to Manley, Neri, or both.
Condition 3: Klosnik does not sit immediately next to Manley.
Condition 4: If Osata sits immediately next to Poirier, Osata does not sit immediately next to Manley.
We need to check each option to see if it satisfies all the conditions.

Option A: Klosnik, Poirier, Neri, Manley, Osata, Londi
Poirier sits next to Neri: Yes (Poirier is 2, Neri is 3).
Londi next to Manley, Neri, or both: Yes (Londi is 6, next to Manley 4).
Klosnik not next to Manley: No (Klosnik 1, Manley 4 are not adjacent).
Osata next to Poirier: No (Osata 5, Poirier 2 are not adjacent).
This option does not violate any conditions.

Option B: Klosnik, Londi, Manley, Poirier, Neri, Osata
Poirier sits next to Neri: Yes (Poirier is 4, Neri is 5).
Londi next to Manley, Neri, or both: Yes (Londi 2, Manley 3 are next to each other).
Klosnik not next to Manley: Yes (Klosnik 1, Manley 3 are not adjacent).
Osata next to Poirier: No (Osata 6, Poirier 4 are not adjacent).
This option does not violate any conditions.

Option C: Klosnik, Londi, Manley, Osata, Poirier, Neri
Poirier sits next to Neri: Yes (Poirier is 5, Neri is 6).
Londi next to Manley, Neri, or both: Yes (Londi 2, Manley 3 are next to each other).
Klosnik not next to Manley: Yes (Klosnik 1, Manley 3 are not adjacent).
Osata next to Poirier: Yes (Osata 4, Poirier 5 are next to each other).
If Osata next to Poirier, Osata not next to Manley: No (Osata 4, Manley 3 are next to each other).
This option violates the condition 4.

Option D: Klosnik, Osata, Poirier, Neri, Londi, Manley
Poirier sits next to Neri: Yes (Poirier is 3, Neri is 4).
Londi next to Manley, Neri, or both: Yes (Londi 5, Manley 6 are next to each other).
Klosnik not next to Manley: Yes (Klosnik 1, Manley 6 are not adjacent).
Osata next to Poirier: Yes (Osata 2, Poirier 3 are next to each other).
If Osata next to Poirier, Osata not next to Manley: Yes (Osata 2, Manley 6 are not adjacent).
This option does not violate any conditions.

Option E: Klosnik, Neri, Londi, Osata, Manley, Poirier
Poirier sits next to Neri: No (Poirier 6, Neri 2 are not adjacent).
This option violates condition 1.

Conclusion
The option which does not violate any stated conditions is Option B: Klosnik, Londi, Manley, Poirier, Neri, Osata.
Correct Answer: B

Problem: A small software firm has four offices, numbered 1, 2, 3, and 4. Each of its offices has exactly one computer and exactly one printer. Each of these eight machines was bought in either 1987, 1988, or 1989. The eight machines were bought in a manner consistent with the following conditions: The computer in each office was bought either in an earlier year than or in the same year as the printer in that office. The computer in office 2 and the printer in office 1 were bought in the same year. The computer in office 3 and the printer in office 4 were bought in the same year. The computer in office 2 and the computer in office 3 were bought in different years. The computer in office 1 and the printer in office 3 were bought in 1988.
Question: If the computer in office 4 was bought in 1988, then which one of the following statements must be true?
options: 
A) The printer in office 1 was bought in 1988.
B) The printer in office 1 was bought in 1989.
C) The computer in office 2 was bought in 1988.
D) The computer in office 3 was bought in 1987.
E) The printer in office 4 was bought in 1989.
Reasoning: To determine which statement must be true if the computer in office 4 was bought in 1988, we need to analyze the given conditions and the purchase years of the computers and printers:

The computer in each office was bought either in an earlier year than or in the same year as the printer in that office.
The computer in office 2 and the printer in office 1 were bought in the same year.
The computer in office 3 and the printer in office 4 were bought in the same year.
The computer in office 2 and the computer in office 3 were bought in different years.
The computer in office 1 and the printer in office 3 were bought in 1988.
Given: The computer in office 4 was bought in 1988.

Let's determine the purchase years for all machines:

Computer 1 (C1) was bought in 1988.
Printer 3 (P3) was bought in 1988.
Computer 4 (C4) was bought in 1988.
Step-by-Step Analysis:
Computer in Office 1 (C1) and Printer in Office 3 (P3):

Both were bought in 1988.
Computer in Office 4 (C4):

Given it was bought in 1988.
The printer in office 4 (P4) must have been bought in 1988 or 1989 (to satisfy the condition that the computer was bought in an earlier year or the same year).
Computer in Office 2 (C2) and Printer in Office 1 (P1):

Both were bought in the same year. This year could be 1987, 1988, or 1989.
Computer in Office 3 (C3) and Printer in Office 4 (P4):

Both were bought in the same year.
Since C4 was bought in 1988, P4 must be bought in 1988 or 1989.
Given C3 and P4 must be in the same year, C3 can be bought in 1988 or 1989.
Computer in Office 2 (C2) and Computer in Office 3 (C3):

They must be bought in different years.
Since C4 was bought in 1988, if C3 is bought in 1988, C2 must be bought in 1987 or 1989.
Logical Deduction:

Let's see the implications of different possible years for C2 and C3:

If C2 is bought in 1987:
P1 must be bought in 1987.
Since C2 is bought in 1987 and P1 is bought in 1987, P1 cannot be bought in 1988 or 1989.
If C2 is bought in 1989:
P1 must be bought in 1989.
This does not contradict any conditions.
Given the conditions, if C2 is bought in 1989, P1 must be 1989.

Therefore, the most consistent solution when C4 is bought in 1988 leads to P1 being bought in 1989.

Conclusion:

If the computer in office 4 was bought in 1988, then the printer in office 1 must have been bought in 1989.
Correct Answer: B

Problem: Arbutus College owns exactly four houses that it leases to faculty or students. Of these houses, no two are exactly the same distance from Arbutus's campus, and each house is either a student house (occupied entirely by students) or a faculty house (occupied entirely by faculty). The lease length for each house is one, two, or three semesters. The following conditions must hold: No student house has a three-semester lease. At least two houses each have longer leases than does the house closest to campus. Every student house (if there are any) is farther from campus than any faculty house (if there are any).
Question: What is the maximum number of houses that could all be student houses with two-semester leases?
options:
A) zero
B) one
C) two
D) three
E) four
Reasoning: To solve this problem, let's carefully analyze the conditions given and determine the maximum number of houses that could all be student houses with two-semester leases.

Conditions:

No student house has a three-semester lease.
At least two houses each have longer leases than the house closest to campus.
Every student house (if there are any) is farther from campus than any faculty house (if there are any).
Interpreting Conditions:

The house closest to campus cannot have the longest lease.
At least two houses must have longer leases than the house closest to campus.
Student houses must be farther from campus than faculty houses.
Objective:

Determine the maximum number of student houses with two-semester leases.
Let's explore the possibilities while adhering to these conditions:

Condition 2: Implies that the house closest to campus cannot have the longest lease and there must be at least two houses with longer leases than the closest house.

If the closest house has a one-semester lease, at least two other houses must have two-semester or three-semester leases.
If the closest house has a two-semester lease, at least two other houses must have three-semester leases (which isn't possible for student houses because of Condition 1).
Strategy:
To maximize the number of student houses with two-semester leases, the house closest to campus must be a faculty house to satisfy Condition 3. This allows student houses to be farther from campus.

Scenario Construction:
Closest House: Faculty house with a one-semester lease.
Remaining Houses: Evaluate how many of these can be student houses with two-semester leases.
The second closest house could be a student house with a two-semester lease.
The third closest house could be a student house with a two-semester lease.
The farthest house could be a student house with a two-semester lease.
Let's break down:

House Closest to Campus (House 1): Faculty house with one-semester lease.
Second House (House 2): Student house with a two-semester lease.
Third House (House 3): Student house with a two-semester lease.
Fourth House (House 4): Student house with a two-semester lease.
Verification:
The house closest to campus (House 1) has the shortest lease, fulfilling Condition 2.
All student houses (House 2, House 3, House 4) have two-semester leases.
All student houses are farther from campus than the faculty house, satisfying Condition 3.
Conclusion:
The maximum number of houses that could all be student houses with two-semester leases is three.
Correct Answer: D

Problem: A six-week literature course is being planned in which six books—F, K, N, O, R, and T—will be discussed. The books will be discussed one at a time, one book per week. In addition, written summaries will be required for one or more of the books. The order in which the books are discussed and the selection of books to be summarized is subject to the following conditions: No two books that are summarized are discussed in consecutive weeks. If N is not summarized, then both R and T are summarized. N is discussed earlier than T, and T is discussed earlier than O. F is discussed earlier than O, and O is discussed earlier than both K and R.
Question: Which one of the following could be the plan for the course, showing the order, from first to last, in which the books are discussed and the choice of books to be summarized?
options:
A) F, N, T, O, R, K; with only T and R summarized
B) F, T, N, O, K, R; with only N and K summarized
C) N, F, T, O, K, R; with only T, O, and R summarized
D) N, T, F, O, K, R; with only T and O summarized
E) N, T, O, F, K, R; with only T and R summarized
Reasoning: Let's analyze the given conditions and the options to determine which one meets all the conditions.

Conditions:

No two books that are summarized are discussed in consecutive weeks.
If N is not summarized, then both R and T are summarized.
N is discussed earlier than T, and T is discussed earlier than O.
F is discussed earlier than O, and O is discussed earlier than both K and R.
Option A: F, N, T, O, R, K; with only T and R summarized
Order: F, N, T, O, R, K
Summarized: T, R
Analysis:

Condition 1: T (week 3) and R (week 5) are not consecutive.
Condition 2: N is not summarized, and both R and T are summarized, satisfying this condition.
Condition 3: N (week 2) is earlier than T (week 3), and T (week 3) is earlier than O (week 4).
Condition 4: F (week 1) is earlier than O (week 4), and O (week 4) is earlier than both K (week 6) and R (week 5).
Valid
Option B: F, T, N, O, K, R; with only N and K summarized
Order: F, T, N, O, K, R
Summarized: N, K
Analysis:

Condition 1: N (week 3) and K (week 5) are not consecutive.
Condition 2: N is summarized, so this condition does not apply.
Condition 3: N (week 3) is not earlier than T (week 2), violating this condition.
Invalid
Option C: N, F, T, O, K, R; with only T, O, and R summarized
Order: N, F, T, O, K, R
Summarized: T, O, R
Analysis:

Condition 1: T (week 3), O (week 4), and R (week 6) include consecutive summaries (T and O), violating this condition.
Invalid
Option D: N, T, F, O, K, R; with only T and O summarized
Order: N, T, F, O, K, R
Summarized: T, O
Analysis:

Condition 1: T (week 2) and O (week 4) are not consecutive.
Condition 2: N is not summarized, and both R and T are summarized. Here, R is not summarized, violating this condition.
Invalid
Option E: N, T, O, F, K, R; with only T and R summarized
Order: N, T, O, F, K, R
Summarized: T, R
Analysis:

Condition 1: T (week 2) and R (week 6) are not consecutive.
Condition 2: N is not summarized, and both R and T are summarized, satisfying this condition.
Condition 3: N (week 1) is earlier than T (week 2), and T (week 2) is earlier than O (week 3).
Condition 4: O (week 3) should be earlier than both K (week 5) and R (week 6), but F (week 4) is in between O and the others, violating the condition.
Invalid
Correct Answer: A

Problem: Three couples—John and Kate, Lewis and Marie, and Nat and Olive have dinner in a restaurant together. Kate, Marie, and Olive are women; the other three are men. Each person orders one and only one of the following kinds of entrees: pork chops, roast beef, swordfish, tilefish, veal cutlet. The six people order in a manner consistent with the following conditions: The two people in each couple do not order the same kind of entree as each other. None of the men orders the same kind of entree as any of the other men. Marie orders swordfish. Neither John nor Nat orders a fish entree. Olive orders roast beef.
Question: Which one of the following statements must be true?
options:
A) One of the men orders pork chops or veal cutlet.
B) One of the men orders swordfish or veal cutlet.
C) Two of the women order tilefish.
D) None of the men orders a fish entree.
E) Exactly one of the women orders a fish entree.
Reasoning: To determine which statement must be true, we need to analyze the given conditions and the possible entrees ordered by each individual. Let's list the conditions and then evaluate the options step-by-step.

Conditions:
Each couple does not order the same kind of entree.
None of the men orders the same kind of entree as any of the other men.
Marie orders swordfish.
Neither John nor Nat orders a fish entree.
Olive orders roast beef.
Individuals and Couples:
John and Kate
Lewis and Marie
Nat and Olive
Ordered Entrees:
Entrees available: pork chops, roast beef, swordfish, tilefish, veal cutlet.
Analysis:
Marie orders swordfish:
Marie: swordfish
Olive orders roast beef:
Olive: roast beef
Neither John nor Nat orders a fish entree:
John and Nat do not order swordfish or tilefish.
Breakdown:
Marie (swordfish) and her husband Lewis must order something different:

Marie: swordfish
Lewis: not swordfish, not the same as other men (possible options: pork chops, veal cutlet, tilefish)
Olive (roast beef) and her husband Nat must order something different:

Olive: roast beef
Nat: not roast beef, not a fish entree (possible options: pork chops, veal cutlet)
John:

Not a fish entree (possible options: pork chops, veal cutlet, roast beef)
Kate and her husband John must order something different:

Kate's options are dependent on what John orders, but John has limited options.
Evaluating Options:
A) One of the men orders pork chops or veal cutlet.

John, Nat, and Lewis are the men.
John and Nat cannot order fish entrees.
Therefore, the only remaining entrees for John and Nat are pork chops, veal cutlet, and roast beef.
Since Olive orders roast beef, Nat cannot order roast beef. Hence, Nat must order either pork chops or veal cutlet.
Similarly, John must order either pork chops, veal cutlet, or roast beef.
This must be true because both John and Nat have no other options apart from pork chops or veal cutlet if they do not order roast beef.
B) One of the men orders swordfish or veal cutlet.

John and Nat cannot order swordfish.
This is not necessarily true for Lewis. Lewis could order tilefish, pork chops, or veal cutlet. There's no restriction forcing Lewis to order swordfish or veal cutlet.
C) Two of the women order tilefish.

Marie orders swordfish, Olive orders roast beef.
Only Kate remains to order tilefish.
Therefore, this is not necessarily true.
D) None of the men orders a fish entree.

This is not necessarily true because Lewis can order tilefish.
E) Exactly one of the women orders a fish entree.

Marie orders swordfish.
Olive does not order a fish entree (roast beef).
Kate can still order a fish entree (tilefish), making it possible that more than one woman orders a fish entree.
This is not necessarily true.
Correct Answer: A

Problem: Hannah spends 14 days, exclusive of travel time, in a total of six cities. Each city she visits is in one of three countries—X, Y, or Z. Each of the three countries has many cities. Hannah visits at least one city in each of the three countries. She spends at least two days in each city she visits. She spends only whole days in any city.
Question: If Hannah visits a combined total of four cities in countries X and Y, what is the greatest total number of days she can spend visiting cities in country Y?
options:
A) 6
B) 7
C) 8
D) 9
E) 10
Reasoning: To solve the problem, we need to maximize the number of days Hannah spends in cities in country Y while adhering to the given constraints. Let's break down the information provided:

Total days spent in cities: 14 days.
Total number of cities visited: 6 cities.
Countries involved: X, Y, Z.
Visits at least one city in each country: Must visit at least one city in X, Y, and Z.
Minimum days in each city: 2 days per city.
Total cities in X and Y combined: 4 cities.
Steps to solve:
Distribute the cities among the countries:

Since Hannah visits a combined total of 4 cities in countries X and Y, she visits the remaining 2 cities in country Z.
At least one city must be visited in each country.
Minimize the days spent in cities in countries X and Z to maximize days in Y:

Each city must have at least 2 days of visit.
Distribute the cities such that the least days are spent in cities in X and Z, maximizing days in Y.
Calculation:
Minimum days in cities in Z:

Visiting 2 cities in Z, minimum days spent = 2 cities * 2 days = 4 days.
Minimum days in cities in X:

Visiting 1 city in X, minimum days spent = 1 city * 2 days = 2 days.
This leaves 1 city to be visited in Y and as many days as possible in Y.
Total days so far:

Days in Z + Days in X = 4 days + 2 days = 6 days.
Remaining days for cities in Y:

Total days available = 14 days.
Days already allocated to X and Z = 6 days.
Remaining days for Y = 14 days - 6 days = 8 days.
Conclusion:
Given the constraints, the greatest total number of days Hannah can spend visiting cities in country Y is 8 days.
Correct Answer: C

Problem: There are exactly seven houses on a street. Each house is occupied by exactly one of seven families: the Kahns, Lowes, Muirs, Newmans, Owens, Piatts, Rutans. All the houses are on the same side of the street, which runs from west to east. The Rutans do not live in the first or the last house on the street. The Kahns live in the fourth house from the west end of the street. The Muirs live next to the Kahns. The Piatts live east of both the Kahns and the Muirs but west of the Lowes.
Question: If the Owens live east of the Kahns, which one of the following pairs of families must live next to each other?
options:
A) the Kahns and the Piatts
B) the Lowes and the Owens
C) the Muirs and the Newmans
D) the Newmans and the Rutans
E) the Owens and the Piatts
Reasoning: To determine which pair of families must live next to each other given the conditions, let's analyze the information step-by-step:

Kahns live in the fourth house from the west end:

Kahns are in house 4.
Rutans do not live in the first or the last house:

Rutans are not in house 1 or house 7.
Muirs live next to the Kahns:

Muirs must be in house 3 or house 5.
Piatts live east of both the Kahns and the Muirs but west of the Lowes:

Piatts are in a house number greater than 4 and 5 (since Muirs could be in house 3 or 5) and less than the house number for the Lowes.
Owens live east of the Kahns:

Owens must be in a house number greater than 4.
Given these conditions, let's deduce the positions of each family:

House 4: Kahns
House 3 or 5: Muirs (since Muirs live next to the Kahns)
House 3 or 5: If Muirs are in house 3, then house 5 is free for another family; if Muirs are in house 5, then house 3 is free for another family.
House 6 or 7: Piatts (since Piatts live east of the Kahns and Muirs but west of the Lowes)
House 6 or 7: If Piatts are in house 6, then house 7 is free for another family; if Piatts are in house 7, then house 6 is free for another family.
House 1 or 2: Rutans (since Rutans do not live in house 1 or house 7)
Given that:

House 1: Rutan cannot be here (by the conditions)
House 7: Rutan cannot be here (by the conditions)
Owens: They must be east of the Kahns (house 4), so they must be in house 5, 6, or 7.
Lowes: Must be east of Piatts, so if Piatts are in house 6, Lowes must be in house 7.
Newmans: We have not placed them yet.
Let's check possible arrangements:

If Muirs are in house 3, the arrangement is:
House 3: Muirs
House 4: Kahns
House 5, 6, or 7: Owens, Piatts, Lowes
This leaves houses 1 and 2 for Rutans and Newmans.

If Muirs are in house 5, the arrangement is:
House 5: Muirs
House 4: Kahns
House 6 or 7: Piatts
House 1 or 2: Rutans
House 6 or 7: Lowes and Owens (since Owens live east of the Kahns, and Lowes east of Piatts)
Given the condition Owens must live east of the Kahns and considering the other constraints:

From the information deduced, the valid pairs next to each other considering the remaining available positions must include:

House 6 or 7: The only positions left that can fit next to each other while following all rules are the Newmans and Rutans.
So the pair that must live next to each other is:
D) the Newmans and the Rutans
Correct Answer: D

Problem: Planes 1, 2, 3, and 4—and no others—are available to fly in an air show. Pilots Anna, Bob, and Cindy are all aboard planes that are flying in the show and they are the only qualified pilots in the show. Copilots Dave, Ed, and Fran are all aboard planes that are flying in the show and they are the only qualified copilots in the show. No plane flies in the show without a qualified pilot aboard. No one but qualified pilots and qualified copilots flies in the show. Anna will only fly in either plane 1 or plane 4. Dave will only fly in either plane 2 or plane 3.
Question: If plane 1 is used, its crew could consist of
options:
A) Anna, Bob, Cindy, Fran
B) Anna, Bob, Ed, Fran
C) Bob, Cindy, Ed, Fran
D) Bob, Cindy, Dave, Ed
E) Bob, Dave, Ed, Fran
Reasoning: Let's analyze the problem step by step with the given conditions:

Available planes: 1, 2, 3, 4.
Qualified pilots: Anna, Bob, Cindy.
Qualified copilots: Dave, Ed, Fran.
Specific conditions:
Anna will only fly in either plane 1 or plane 4.
Dave will only fly in either plane 2 or plane 3.
No plane flies without a qualified pilot aboard.
Only qualified pilots and copilots are aboard the planes.
We need to determine a possible crew for plane 1. Since Anna will only fly in plane 1 or plane 4, we can consider her as a potential pilot for plane 1. Dave will not be available for plane 1 because he can only fly in planes 2 or 3.

Let's evaluate each option to see if it satisfies these constraints:

Option A: Anna, Bob, Cindy, Fran

This option includes all three pilots (Anna, Bob, Cindy) on plane 1, which leaves no pilots for the other planes, violating the rule that every plane must have a qualified pilot.
Invalid.
Option B: Anna, Bob, Ed, Fran

Anna is a pilot, which is allowed because she can fly in plane 1.
Bob is another pilot. It’s possible to have more than one pilot listed for a plane as long as other planes still meet their requirements.
Ed and Fran are copilots, fulfilling the requirement for copilots.
There are still pilots (Cindy) and copilots (Dave) available for the other planes.
Valid.
Option C: Bob, Cindy, Ed, Fran

This option does not include Anna, who is required to fly in plane 1 or plane 4.
Invalid.
Option D: Bob, Cindy, Dave, Ed

Dave can only fly in planes 2 or 3, not in plane 1.
Invalid.
Option E: Bob, Dave, Ed, Fran

Dave can only fly in planes 2 or 3, not in plane 1.
Invalid.
Given the analysis, only Option B: Anna, Bob, Ed, Fran meets all the criteria and constraints.

Thus, the correct answer is:

B) Anna, Bob, Ed, Fran.
Correct Answer: B

Problem: The Mammoth Corporation has just completed hiring nine new workers: Brandt, Calva, Duvall, Eberle, Fu, Garcia, Haga, Irving, and Jessup. Fu and Irving were hired on the same day as each other, and no one else was hired that day. Calva and Garcia were hired on the same day as each other, and no one else was hired that day. On each of the other days of hiring, exactly one worker was hired. Eberle was hired before Brandt. Haga was hired before Duvall. Duvall was hired after Irving but before Eberle. Garcia was hired after both Jessup and Brandt. Brandt was hired before Jessup.
Question: Exactly how many workers were hired before Jessup?
options:
A) 6
B) 5
C) 4
D) 3
E) 2
Reasoning: To determine how many workers were hired before Jessup, let's analyze the given conditions:

Fu and Irving were hired on the same day, as were Calva and Garcia.
Eberle was hired before Brandt.
Haga was hired before Duvall.
Duvall was hired after Irving but before Eberle.
Garcia was hired after both Jessup and Brandt.
Brandt was hired before Jessup.
Analysis:
From condition 1:

Fu and Irving were hired on the same day.
Calva and Garcia were hired on the same day.
This means 4 workers (Fu, Irving, Calva, and Garcia) were hired on the same day, leaving 5 workers to be hired individually.
From conditions 2, 3, and 4:

Eberle was hired before Brandt, and Haga was hired before Duvall.
Duvall was hired after Irving but before Eberle.
This implies the order of hiring must be Irving, Duvall, Eberle, Brandt, Haga.
From condition 5:

Garcia was hired after both Jessup and Brandt.
This means Jessup was hired before Garcia.
From condition 6:

Brandt was hired before Jessup.
Conclusion:
Given the analysis, the order of hiring must be:

Irving
Duvall
Eberle
Brandt
Haga
Jessup
Fu
Calva
Garcia
So, 6 workers (Irving, Duvall, Eberle, Brandt, Haga, and Jessup) were hired before Jessup.

Thus, the correct answer is:

A) 6
Correct Answer: A

Problem: Meena has six colored pencils—green, maroon, orange, red, white, and yellow. She sketches a drawing using exactly five of the six pencils, one pencil at a time. The following conditions must hold: No pencil is used more than once. Either the maroon or the yellow pencil is not used. The red pencil is used at some time before the green. The red pencil is used at some time before either the orange or the yellow, but not before both. The green pencil is used at some time before either the maroon or the white, but not before both.
Question: Which one of the following could be an accurate list of the pencils used, from first to fifth?
options:
A) orange, green, red, maroon, yellow
B) red, green, orange, white, maroon
C) red, orange, maroon, white, green
D) white, red, orange, green, maroon
E) white, yellow, orange, green, red
Reasoning: Let's reassess the options with a more detailed analysis based on the conditions provided:

Either the maroon or the yellow pencil is not used.
The red pencil is used at some time before the green.
The red pencil is used at some time before either the orange or the yellow, but not before both.
The green pencil is used at some time before either the maroon or the white, but not before both.
Detailed Analysis
Option A: orange, green, red, maroon, yellow
Maroon and yellow are both used, violating the first condition.
Red is used after green, violating the second condition.
Invalid.
Option B: red, green, orange, white, maroon
Either maroon or yellow is not used: Yellow is not used, satisfying the first condition.
Red is used before green, satisfying the second condition.
Red is used before orange, satisfying part of the third condition. Yellow is not used, so this part is trivially satisfied.
Green is used before white, but green is used before maroon as well, violating the fourth condition (green should come before only one of maroon or white).
Invalid.
Option C: red, orange, maroon, white, green
Either maroon or yellow is not used: Yellow is not used, satisfying the first condition.
Red is used before green, satisfying the second condition.
Red is used before orange, and yellow is not used, so the third condition is satisfied.
Green is used after both maroon and white, violating the fourth condition (green should come before only one of maroon or white, not both).
Invalid.
Option D: white, red, orange, green, maroon
Either maroon or yellow is not used: Yellow is not used, satisfying the first condition.
Red is used before green, satisfying the second condition.
Red is used before orange, and yellow is not used, satisfying the third condition.
Green is used before maroon, and white is used before green, satisfying the fourth condition since green comes before only one of maroon or white.
Valid.
Option E: white, yellow, orange, green, red
Maroon is not used, satisfying the first condition.
Red is used after green, violating the second condition.
Red is used after both orange and yellow, violating the third condition.
Invalid.
Conclusion:
Given the detailed conditions analysis, Option D satisfies all the conditions.
Correct Answer: D
"""
    




    message.append({"role": "system", "content": cot_samples})
    #content = data[index]['context'] +' ' + data[index]['question']+' '
    #content += ' '.join(data[index]['options'])
    d = {}
    d["role"] = "user"
    d["content"] = "Problem: \n"+data[index]['context']+"\n"+"Question: \n"+data[index]['question']+"\n"+"options:\n"+'\n'.join(data[index]['options'])+"\n" 
   
    
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
