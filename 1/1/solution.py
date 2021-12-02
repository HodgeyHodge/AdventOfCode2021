file = open("testinput.txt", "r")

increases = 0
prevDepth = 0

for line in file:
    if (int(line) > prevDepth):
        increases += 1
    prevDepth = int(line)

print(increases - 1)

file.close()
