file = open("../input.txt", "r")

lines = 0
width = len(file.readline()) - 1
bitsum = [0] * width

for line in file:
    lines += 1
    for i in range(0, width):
        bitsum[i] += int(line[i])

print([bitsum[i] > lines/2 for i in range(0, width)])

file.close()
