
filename = 'input.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

width = len(lines[0])
height = len(lines)
risk = 0

for i in range(0, height):
    for j in range (0, width):
        if ((i == 0 or lines[i][j] < lines[i - 1][j]) and
            (i == height - 1 or lines[i][j] < lines[i + 1][j]) and
            (j == 0 or lines[i][j] < lines[i][j - 1]) and
            (j == width - 1 or lines[i][j] < lines[i][j + 1])):
            risk += int(lines[i][j])+ 1

print(risk)
