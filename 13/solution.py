def read_file(filename):
    dots = set()
    instructions = []
    with open(filename) as file:
        section = 0
        for line in file:
            if len(line) == 1:
                section += 1
                continue
            if section == 0:
                dots.add(tuple(int(coord) for coord in line.strip('\n').split(',')))
            else:
                instruction = line.replace('fold along ', '').strip('\n').split('=')
                instructions.append(tuple([instruction[0], int(instruction[1])]))
    return dots, instructions

def part_one(dots, instructions):
    direction = instructions[0][0]
    position = instructions[0][1]
    if direction == 'x':
        folded_dots = set([(2 * position - z[0], z[1]) if z[0] > position else (z[0], z[1]) for z in dots])
    else:
        folded_dots = set([(z[0], 2 * position - z[1]) if z[1] > position else (z[0], z[1]) for z in dots])
    return folded_dots

def part_two(dots, instructions):
    for instruction in instructions:
        if instruction[0] == 'x':
            folded_dots = set([(2 * instruction[1] - z[0], z[1]) if z[0] > instruction[1] else (z[0], z[1]) for z in dots])
        else:
            folded_dots = set([(z[0], 2 * instruction[1] - z[1]) if z[1] > instruction[1] else (z[0], z[1]) for z in dots])
        dots = folded_dots
    return dots

def pretty_print_dots(dots):
    width = max([dot[0] for dot in dots])
    height = max([dot[1] for dot in dots])
    for j in range(0, height + 1):
        for i in range(0, width + 1):
            print('#' if (i, j) in dots else ' ', end='')
        print('')
    
print('Part one test data:', len(part_one(*read_file("testinput.txt"))))
print('Part one live data:', len(part_one(*read_file("input.txt"))))

print('Part two test data:')
pretty_print_dots(part_two(*read_file("testinput.txt")))

print('Part two live data:')
pretty_print_dots(part_two(*read_file("input.txt")))


