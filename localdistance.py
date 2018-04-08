with open("./data/dictionary.txt", "r") as f:
    dictionary = set()
    for item in f:
        dictionary.add(item[:-1])

def print_table(table):
    for row in table:
        print(row)

def localdistance(token):
    """calculate localdistance for each word in dictionary to token using Needleman–Wunsch algorithm"""
    # [row number][col number]
    # parameters: [m, i, d, r] = [+1, -1, -1, -1]

    if token in dictionary:
        return token

    matched_word_list = []
    max_score = 0

    for word in dictionary:
        first_row = []
        dp_table = [first_row]
        max_word_score = 0

        for i in range(len(token)+1):
            first_row.append(-1 * i)

        for i in range(1, len(word)+1):
            dp_table.append([-1 * i])

        for row_index in range(1, len(dp_table)):
            word_index = row_index - 1
            for col_index in range(1, len(dp_table[0])):
                token_index = col_index - 1
                up, left, diag = dp_table[row_index-1][col_index], dp_table[row_index][col_index-1], dp_table[row_index-1][col_index-1]
                if word[word_index] == token[token_index]:
                    score = max(up-1, left-1, diag+1, 0)
                else:
                    score = max(up-1, left-1, diag-1, 0)
                dp_table[row_index].append(score)
                if score > max_word_score:
                    max_word_score = score
                    # if max_word_score == len(token):
                    #     return word

        if max_word_score > max_score:
            max_score = max_word_score
            # if max_score == len(token):
            #     return word
            matched_word_list = [word]
        elif max_word_score == max_score:
            matched_word_list.append(word)
    return matched_word_list

with open("./data/misspell1.txt", "r") as f:
    for word in f:
        print(localdistance(word))

# word = input('Enter misspelled word: ')
# print(localdistance(word, {'deaden', 'blenders', 'commodity','addendum', 'end', 'leader', 'leant', 'lent', 'lemonade', 'pleading'}))
