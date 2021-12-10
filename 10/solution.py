
filename = "input.txt"

prices = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '': 0
} 

def get_first_closer(string):
    positions = [p for p in [string.find(c) for c in [')', ']', '}', '>']] if p > -1]
    return string[min(positions)] if positions else ''

def essentialise(string):
    start_length = len(string)
    string = string.replace('<>', '')
    string = string.replace('{}', '')
    string = string.replace('[]', '')
    string = string.replace('()', '')
    end_length = len(string)
    return string if start_length == end_length else essentialise(string)

cost = 0
with open(filename) as file:
    for line in [line.strip('\n') for line in file]:
        line = essentialise(line)
        cost += prices[get_first_closer(line)]
print(cost)
