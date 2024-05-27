import re
import argparse
import csv

correct_answers = []
parser = argparse.ArgumentParser(description="Parse a text file for correct answers.")
parser.add_argument('filepath', help="The path to the text file to parse.")
args = parser.parse_args()

with open(args.filepath, 'r') as file:
    text = file.read()

blocks = re.findall(r'LLama3 Response begins:(.*?)Response ends:', text, re.DOTALL)

for block in blocks:
    match = re.search(r'correct answer.*?(A\)|B\)|C\)|D\)|E\))', block)
    if match:
        correct_answers.append(match.group(1).replace(")", ""))
    else:
        # Check for single occurrence of A), B), C), D), or E)
        single_match = re.search(r'(A\)|B\)|C\)|D\)|E\))', block)
        if single_match:
            correct_answers.append(single_match.group(1).replace(")", ""))
        else:
            correct_answers.append("none")

print(correct_answers)

with open('parser_parsed_results.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for answer in correct_answers:
        writer.writerow([answer])
