
def pretty_print(f):
    for line in f:
        print(''.join(char for char in line))

def part_one(filename):
    with open(filename) as file:
        f = [[char for char in line.strip('\n')] for line in file]
    height = len(f)
    width = len(f[0])
    
    iterations = 0
    while True:
        movements = [[], []]
        for i in range(0, height):
            for j in range(0, width):
                if f[i][j] == '>' and f[i][(j+1)%(width)] == '.':
                    movements[0].append((i, j))
        for m in movements[0]:
            f[m[0]][m[1]] = '.'
            f[m[0]][(m[1]+1)%(width)] = '>'
        
        for i in range(0, height):
            for j in range(0, width):
                if f[i][j] == 'v' and f[(i+1)%(height)][j] == '.':
                    movements[1].append((i, j))
        for m in movements[1]:
            f[m[0]][m[1]] = '.'
            f[(m[0]+1)%(height)][m[1]] = 'v'
    
        iterations += 1
    
        if len(movements[0]) == 0 and len(movements[1]) == 0:
            print(f'At iteration {iterations}, nothing happened...')
            break

part_one('testinput.txt')
part_one('input.txt')