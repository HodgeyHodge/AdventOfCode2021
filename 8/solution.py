import re

filename = "input.txt"
pattern = r"(\b[a-g]{2,4}\b)|(\b[a-g]{7}\b)"

with open(filename) as file:
    i = file.readline().find('|')

with open(filename) as file:
    print(sum([len(re.findall(pattern, line[i:])) for line in file]))


