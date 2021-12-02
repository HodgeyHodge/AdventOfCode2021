file = open("input.txt", "r")

horizontal = 0
vertical = 0

for line in file:
    if (line.startswith('forward ')):
        horizontal += int(line[8:])
    elif (line.startswith('down ')):
        vertical -= int(line[5:])
    elif (line.startswith('up ')):
        vertical += int(line[3:])

print(vertical * horizontal)

file.close()
