
def decode(a):
    if a == 'w': return 0
    if a == 'x': return 1
    if a == 'y': return 2
    if a == 'z': return 3
    else: return -1

def run(program, number):
    output = [0, 0, 0, 0]
    i = 0
    for instruction in program:
        instruction = instruction.split(' ')
        if instruction[0] == 'inp':
            output[decode(instruction[1])] = int(number[i])
            i += 1
        elif instruction[0] == 'add':
            if decode(instruction[2]) == -1:
                output[decode(instruction[1])] += int(instruction[2])
            else:
                output[decode(instruction[1])] += output[decode(instruction[2])]
        elif instruction[0] == 'mul':
            if decode(instruction[2]) == -1:
                output[decode(instruction[1])] *= int(instruction[2])
            else:
                output[decode(instruction[1])] *= output[decode(instruction[2])]
        elif instruction[0] == 'div':
            if decode(instruction[2]) == -1:
                output[decode(instruction[1])] = int(output[decode(instruction[1])] / int(instruction[2]))
            else:
                output[decode(instruction[1])] = int(output[decode(instruction[1])] / output[decode(instruction[2])])
        elif instruction[0] == 'mod':
            if decode(instruction[2]) == -1:
                output[decode(instruction[1])] = output[decode(instruction[1])] % int(instruction[2])
            else:
                output[decode(instruction[1])] = output[decode(instruction[1])] % output[decode(instruction[2])]
        elif instruction[0] == 'eql':
            if decode(instruction[2]) == -1:
                output[decode(instruction[1])] = int(output[decode(instruction[1])] == int(instruction[2]))
            else:
                output[decode(instruction[1])] = int(output[decode(instruction[1])] == output[decode(instruction[2])])
    return output





testprogram1 = ['inp x', 'mul x -1']
testprogram2 = ['inp z', 'inp x', 'mul z 3', 'eql z x']
testprogram3 = ['inp w', 'add z w', 'mod z 2', 'div w 2', 'add y w', 'mod y 2', 'div w 2', 'add x w', 'mod x 2', 'div w 2', 'mod w 2']



assert(run(['inp w', 'inp x', 'add w x'], '25') == [7, 5, 0, 0])

assert(run(['inp w', 'add w 2'], '2') == [4, 0, 0, 0])

assert(run(['inp w', 'inp x', 'mul w x'], '23') == [6, 3, 0, 0])

assert(run(['inp w', 'mul w 2'], '2') == [4, 0, 0, 0])

assert(run(['inp w', 'inp x', 'div w x'], '32') == [1, 2, 0, 0])
assert(run(['inp w', 'inp x', 'div w x'], '42') == [2, 2, 0, 0])
assert(run(['inp w', 'inp x', 'div w x'], '52') == [2, 2, 0, 0])

assert(run(['inp w', 'div w 2'], '5') == [2, 0, 0, 0])
assert(run(['inp w', 'div w 2'], '6') == [3, 0, 0, 0])
assert(run(['inp w', 'div w 2'], '7') == [3, 0, 0, 0])

assert(run(['inp w', 'inp x', 'mod w x'], '63') == [0, 3, 0, 0])
assert(run(['inp w', 'inp x', 'mod w x'], '73') == [1, 3, 0, 0])
assert(run(['inp w', 'inp x', 'mod w x'], '83') == [2, 3, 0, 0])

assert(run(['inp w', 'mod w 3'], '6') == [0, 0, 0, 0])
assert(run(['inp w', 'mod w 3'], '7') == [1, 0, 0, 0])
assert(run(['inp w', 'mod w 3'], '8') == [2, 0, 0, 0])

assert(run(['inp w', 'inp x', 'eql w x'], '22') == [1, 2, 0, 0])
assert(run(['inp w', 'inp x', 'eql w x'], '29') == [0, 9, 0, 0])

assert(run(['inp w', 'eql w 3'], '3') == [1, 0, 0, 0])
assert(run(['inp w', 'eql w 3'], '4') == [0, 0, 0, 0])

assert(run(testprogram1, '5')[1] == -5)
assert(run(testprogram2, '26')[3] == 1)
assert(run(testprogram2, '39')[3] == 1)
assert(run(testprogram2, '11')[3] == 0)
assert(run(testprogram2, '19')[3] == 0)

assert(run(testprogram3, '1') == [0, 0, 0, 1])
assert(run(testprogram3, '2') == [0, 0, 1, 0])
assert(run(testprogram3, '3') == [0, 0, 1, 1])
assert(run(testprogram3, '4') == [0, 1, 0, 0])
assert(run(testprogram3, '5') == [0, 1, 0, 1])
assert(run(testprogram3, '6') == [0, 1, 1, 0])
assert(run(testprogram3, '7') == [0, 1, 1, 1])
assert(run(testprogram3, '8') == [1, 0, 0, 0])
assert(run(testprogram3, '9') == [1, 0, 0, 1])

with open('input.txt') as file:
    liveprogram = [l.strip('\n') for l in file]

print(run(liveprogram, '91897399498995'))
print(run(liveprogram, '51121176121391'))


