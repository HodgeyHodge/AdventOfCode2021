import re
from functools import reduce

filename = "input.txt"

def word_pattern(n):
    return r"(\b[a-g]{" + str(n) + r"}\b)"

with open(filename) as file:
    i = file.readline().find('|')

number_codes = {}
total = 0

with open(filename) as file:
    for line in file:
        number_codes[1] = ''.join(sorted(re.search(word_pattern(2), line[:i]).group()))
        number_codes[7] = ''.join(sorted(re.search(word_pattern(3), line[:i]).group()))
        number_codes[4] = ''.join(sorted(re.search(word_pattern(4), line[:i]).group()))
        number_codes[8] = ''.join(sorted(re.search(word_pattern(7), line[:i]).group()))

        length_5_strings = [''.join(sorted(x)) for x in re.findall(word_pattern(5), line[:i])]
        length_6_strings = [''.join(sorted(x)) for x in re.findall(word_pattern(6), line[:i])]

        number_codes[2] = ''.join(sorted([x for x in length_5_strings if len(''.join(char for char in 'abcdefg' if (char not in number_codes[4] and char in x))) == 3][0]))
        number_codes[9] = ''.join(sorted([x for x in length_6_strings if len(''.join(char for char in 'abcdefg' if (char not in number_codes[4] and char in x))) == 2][0]))
        
        top_right = ''.join(char for char in 'abcdefg' if char in number_codes[1] and char in number_codes[2])
        
        number_codes[5] = ''.join(sorted([x for x in length_5_strings if top_right not in x][0]))
        number_codes[6] = ''.join(sorted([x for x in length_6_strings if top_right not in x][0]))

        number_codes[3] = [x for x in length_5_strings if x != number_codes[2] and x != number_codes[5]][0]
        number_codes[0] = [x for x in length_6_strings if x != number_codes[6] and x != number_codes[9]][0]
        
        solution_code = [''.join(sorted(w)) for w in line[i + 2:].strip('\n').split(' ')]
        number_codes_inv = {v: k for k, v in number_codes.items()}

        total += 1000 * number_codes_inv[solution_code[0]] + 100 * number_codes_inv[solution_code[1]] + 10 * number_codes_inv[solution_code[2]] + number_codes_inv[solution_code[3]]

print(total)




