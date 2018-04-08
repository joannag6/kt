import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument("filename1", help="path of the correct file",
                    type=str)
parser.add_argument("filename2", help="path of the misspelled file",
                    type=str)
args = parser.parse_args()

correct = []

total_attempts = 0
total_words = 0

with open(args.filename1, "r") as f1:
    with open(args.filename2, "r") as f2:
        for word in f1:
            # if word == f2.readline(): # correct
            line = ast.literal_eval(f2.readline())
            total_attempts += len(line)
            total_words += 1
            if word[:-1] in line: # precision/recall
                correct.append(word)

print('Precision: ' + str(len(correct)/total_attempts))
print('Recall: ' + str(len(correct)/total_words))
