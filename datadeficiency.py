wrongindices = set()
dictionary = set()
with open("./data/dictionary.txt", "r") as f:
    for item in f:
        dictionary.add(item[:-1])
    f.close()

# number of misspelled entries that do appear in the dictionary
notmisspelled = set()
with open("./data/misspell.txt", "r") as f:
    i = 0
    for word in f:
        if word[:-1] in dictionary:
            notmisspelled.add(word[:-1])
            wrongindices.add(i)
        i += 1
    f.close()
print("number of misspelled entries that do appear in the dictionary: " + str(len(notmisspelled)))

# number of correct entries that don’t appear in the dictionary
notcorrect = set()
with open("./data/correct.txt", "r") as f:
    i = 0
    for word in f:
        if word[:-1] not in dictionary:
            notcorrect.add(word[:-1])
            wrongindices.add(i)
        i += 1
    f.close()
print("number of correct entries that don’t appear in the dictionary: " + str(len(notcorrect)))

# number of correct spellings are the same as the “misspelling”
same = set()
with open("./data/correct.txt", "r") as correct:
    with open("./data/misspell.txt", "r") as misspell:
        i = 0
        for word in correct:
            if word == misspell.readline():
                same.add(word[:-1])
                wrongindices.add(i)
            i += 1
    misspell.close()
    correct.close()
print("number of correct spellings are the same as the 'misspelling': " + str(len(same)))


print("number of deficient data in dataset: " + str(len(wrongindices)))
print(sorted(wrongindices))
