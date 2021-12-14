from math import ceil

def read_file(filename):
    with open(filename) as file:
        input_ = file.read().split('\n\n')
    pairs = {}
    for pair in (input_[0][i:i+2] for i in range(0, len(input_[0]) - 1)):
        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1
    instructions = {}
    for i in input_[1].split('\n'):
        i = i.split(' -> ')
        instructions[i[0]] = [i[0][0] + i[1], i[1] + i[0][1]]
    return pairs, instructions

def iterate(pairs, instructions, n):
    for i in range(0, n):
        new_pairs = {}
        for pair in pairs:
            if instructions[pair][0] not in new_pairs:
                new_pairs[instructions[pair][0]] = pairs[pair]
            else:
                new_pairs[instructions[pair][0]] += pairs[pair]
            if instructions[pair][1] not in new_pairs:
                new_pairs[instructions[pair][1]] = pairs[pair]
            else:
                new_pairs[instructions[pair][1]] += pairs[pair]
        pairs = new_pairs
    return new_pairs

def recover_frequencies(pairs):
    frequencies = {}
    for pair in pairs:
        if pair[0] not in frequencies:
            frequencies[pair[0]] = pairs[pair]
        else:
            frequencies[pair[0]] += pairs[pair]
        if pair[1] not in frequencies:
            frequencies[pair[1]] = pairs[pair]
        else:
            frequencies[pair[1]] += pairs[pair]
    return {key: ceil(frequencies[key]/2) for key in frequencies} #every element is double-counted except the first and last


pairs, instructions = read_file('input.txt')
pairs = iterate(pairs, instructions, 10)
frequencies = recover_frequencies(pairs)
print(max([frequencies[f] for f in frequencies]) - min([frequencies[f] for f in frequencies]))
pairs = iterate(pairs, instructions, 30)
frequencies = recover_frequencies(pairs)
print(max([frequencies[f] for f in frequencies]) - min([frequencies[f] for f in frequencies]))





