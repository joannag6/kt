import random
from collections import defaultdict
# aehiouwy →    0 (vowels)
# bpfv     →    1 (labials)
# cgjkqsxz →    2 (misc: fricatives, velars, etc.)
# dt       →    3 (dentals)
# l        →    4 (lateral)
# mn       →    5 (nasals)
# r        →    6 (rhotic)
soundex_dict = {}
for char in 'bpfv':
    soundex_dict[char] = '1'
for char in 'cgjkqsxz':
    soundex_dict[char] = '2'
for char in 'dt':
    soundex_dict[char] = '3'
for char in 'l':
    soundex_dict[char] = '4'
for char in 'mn':
    soundex_dict[char] = '5'
for char in 'r':
    soundex_dict[char] = '6'

# Except for initial character, translate string characters according to table
# Remove duplicates (e.g. 4444 → 4)
# Remove 0s
# Truncate to four symbols

def soundex(word):
    final = word[0]
    prev = ''
    for char in word[1:]:
        char = char.lower()
        if char not in soundex_dict or char in "aehiouwy":
            continue
        if soundex_dict[char] == prev:
            continue
        final += soundex_dict[char]
        prev = soundex_dict[char]
    return final.ljust(4,'0')[:4]

with open("./data/dictionary.txt", "r") as f:
    dictionary = defaultdict(set)
    for item in f:
        dictionary[soundex(item[:-1])].add(item[:-1])

with open("./data/misspell.txt", "r") as f:
    for word in f:
        lst = dictionary[soundex(word[:-1])]
        if lst:
            print(random.sample(lst, 1)[0])
        else:
            print(" ")
