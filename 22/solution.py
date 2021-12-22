
def load_file(filename):
    output = []
    with open(filename) as file:
        for line in file:
            power = 1 if line.split(' ')[0] == 'on' else 0
            coords = tuple(tuple([int(coord.split('..')[0][2:]), int(coord.split('..')[1])]) for coord in line.strip('\n').split(' ')[1].split(','))
            output.append((power, coords))
    return output

def overlap(i, j):
    if i[1][0][0] <= j[1][0][1] and i[1][0][1] >= j[1][0][0] and \
       i[1][1][0] <= j[1][1][1] and i[1][1][1] >= j[1][1][0] and \
       i[1][2][0] <= j[1][2][1] and i[1][2][1] >= j[1][2][0]:
        return (
            (max([i[1][0][0], j[1][0][0]]), min([i[1][0][1], j[1][0][1]])),
            (max([i[1][1][0], j[1][1][0]]), min([i[1][1][1], j[1][1][1]])),
            (max([i[1][2][0], j[1][2][0]]), min([i[1][2][1], j[1][2][1]])))

def volume(i):
    return (1 + i[1][0][1] - i[1][0][0]) * (1 + i[1][1][1] - i[1][1][0]) * (1 + i[1][2][1] - i[1][2][0])

def quality(i):
    if i[0][0] == 0:
        return 0
    else:
        return (-1) ** (len(i[0]) + 1)
    


cuboids = load_file('input2.txt')

print('cuboids in:')
for cuboid in cuboids:
    print(cuboid)

instructions = []
for next_cuboid in cuboids:
    new_instructions = []
    if next_cuboid[0]:
        new_instructions.append(([next_cuboid[0]], next_cuboid[1]))
    for instruction in instructions:
        #print(f'checking for overlap between {next_cuboid} and {instruction}')
        next_overlap = overlap(next_cuboid, instruction)
        #print(f'found overlap between {next_cuboid} and {instruction}: {next_overlap}, {instruction[0]}, {next_cuboid[0]}')
        if next_overlap is not None:
            new_instruction = (instruction[0] + [next_cuboid[0]], next_overlap)
            #print(f'inserting new instruction: {new_instruction}')
            new_instructions.append(new_instruction)
    instructions.extend(new_instructions)

lights_on = 0
print('instructions out:')
for instruction in instructions:
    #print(instruction, volume(instruction), quality(instruction))
    lights_on += quality(instruction) * volume(instruction)
print(lights_on)


