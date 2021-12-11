def step(field, flashes):
    #increment octopus energy
    field = [[position + 1 for position in row] for row in field]
    
    #dissipate flashing octopus energy
    while max([position for row in field for position in row]) > 9:
        field, flashes = flash(field, flashes)

    #flashed octopodes get zeroed
    for i in range(0, height):
        for j in range(0, width):
            if field[i][j] < 0:
                field[i][j] = 0

    return field, flashes

def flash(field, flashes):
    for i in range(0, height):
        for j in range(0, width):
            if field[i][j] > 9:
                flashes += 1
                field[i][j] = -99
                if j + 1 < width:
                    field[i][j + 1] += 1
                if i + 1 < height and j + 1 < width:
                    field[i + 1][j + 1] += 1
                if i + 1 < height:
                    field[i + 1][j] += 1
                if i + 1 < height and j - 1 >= 0:
                    field[i + 1][j - 1] += 1
                if j - 1 >= 0:
                    field[i][j - 1] += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    field[i - 1][j - 1] += 1
                if i - 1 >= 0:
                    field[i - 1][j] += 1
                if i - 1 >= 0 and j + 1 < width:
                    field[i - 1][j + 1] += 1
    return field, flashes


filename = "input.txt"

#part one

with open(filename) as file:
    field = [[int(c) for c in line.strip('\n')] for line in file.readlines()]
    
width = len(field[0])
height = len(field)

flashes = 0
for i in range(0, 100):
    field, flashes = step(field, flashes)
print(flashes)

#part two

with open(filename) as file:
    field = [[int(c) for c in line.strip('\n')] for line in file.readlines()]
    
width = len(field[0])
height = len(field)

flashes = 0
iterations = 0
while True:
    field, flashes = step(field, flashes)
    iterations += 1
    if max([position for row in field for position in row]) == 0:
        print(iterations)
        break





