file = open("input.txt", "r")

increases = 0
lineNumber = 0
depthDict = {-3: 0, -2: 0, -1: 0, 0: 0}

for line in file:
    lineNumber += 1
    
    depthDict[-3] = depthDict[-2]
    depthDict[-2] = depthDict[-1] 
    depthDict[-1] = depthDict[0]
    depthDict[0] = int(line)

    if (lineNumber < 4):
        continue
    
    if (depthDict[0] > depthDict[-3]):
        increases += 1

print(increases)

file.close()
