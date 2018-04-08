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
            wordlist = []
            line = f2.readline()
            while(not "Grand Total: " in line):
                wordlist.append(line[:-1])
                line = f2.readline()
            total_attempts += len(wordlist)
            total_words += 1
            if word[:-1] in wordlist: # precision/recall
                correct.append(word)

print('Precision: ' + str(len(correct)/total_attempts))
print('Recall: ' + str(len(correct)/total_words))
