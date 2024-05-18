import re
import argparse

correct_answers = []
parser = argparse.ArgumentParser(description="Parse a text file for correct answers.")
parser.add_argument('filepath', help="The path to the text file to parse.")
args = parser.parse_args()

with open(args.filepath, 'r') as file:
    text = file.read()

blocks = re.findall(r'LLama3 Response begins:(.*?)Response ends:', text, re.DOTALL)

for block in blocks:
    match = re.search(r'correct answer.*?(A\)|B\)|C\)|D\))', block)
    if match:
        correct_answers.append(match.group(1).replace(")", ""))
    else:
        correct_answers.append("none")

print(correct_answers)
