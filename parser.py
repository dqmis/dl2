import re
import argparse

correct_answers = []
parser = argparse.ArgumentParser(description="Parse a text file for correct answers.")
parser.add_argument('filepath', help="The path to the text file to parse.")
args = parser.parse_args()

with open(args.filepath, 'r') as file:
    text = file.read()

pattern = r'(A\)|B\)|C\)|D\)|E\))'
matches = re.findall(pattern, text)
correct_answers_matches = re.findall(r'The correct answer is (A\)|B\)|C\)|D\)|E\))', text)

for correct_answer in correct_answers_matches:
    if correct_answer in matches:
        correct_answers.append(correct_answer.replace(")", ""))

print(correct_answers)