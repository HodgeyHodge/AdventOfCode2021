
filename = "input.txt"

prices = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
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

costs = []
with open(filename) as file:
    for line in [line.strip('\n') for line in file]:
        cost = 0
        line = essentialise(line)
        if get_first_closer(line) == '':
            for char in reversed(line):
                cost *= 5
                cost += prices[char]
            costs.append(cost)

print(sorted(costs))
print(sorted(costs)[int((len(costs) - 1) / 2)])
