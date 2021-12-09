
def discover_basin(basin):
    #print('processing basin:', basin)
    newpoints = []
    for point in basin:
        i = point[0]
        j = point[1]

        #print('processing point: ', point, 'value', lines[i][j])
        
        if i > 0 and int(lines[i][j]) < int(lines[i - 1][j]) and int(lines[i - 1][j]) < 9:
            #print('adding point:', i - 1, j, 'value', lines[i - 1][j])
            newpoints.append((i - 1, j))

        if i < height - 1 and int(lines[i][j]) < int(lines[i + 1][j]) and int(lines[i + 1][j]) < 9:
            #print('adding point:', i + 1, j, 'value', lines[i + 1][j])
            newpoints.append((i + 1, j))

        if j > 0 and int(lines[i][j]) < int(lines[i][j - 1]) and int(lines[i][j - 1]) < 9:
            #print('adding point:', i, j - 1, 'value', lines[i][j - 1])
            newpoints.append((i, j - 1))
            
        if j < width - 1 and int(lines[i][j]) < int(lines[i][j + 1]) and int(lines[i][j + 1]) < 9:
            #print('adding point:', i, j + 1, 'value', lines[i][j + 1])
            newpoints.append((i, j + 1))

    #print('newpoints:', newpoints)
    #print('before:', basin)
    basin.update(newpoints)
    #print('after:', basin)


filename = 'input.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

width = len(lines[0])
height = len(lines)
basins = []

for i in range(0, height):
    for j in range (0, width):
        if ((i == 0 or lines[i][j] < lines[i - 1][j]) and
            (i == height - 1 or lines[i][j] < lines[i + 1][j]) and
            (j == 0 or lines[i][j] < lines[i][j - 1]) and
            (j == width - 1 or lines[i][j] < lines[i][j + 1])):
            basins.append(set([(i, j)]))

for i in range(0, 20):
    for b in basins:
        discover_basin(b)
    sizes = [len(b) for b in basins]
    sizes.sort(reverse = True)
    print(sizes[0:3])
