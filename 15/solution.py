
def read_file(filename):
    with open(filename) as file:
        return [[int(i) for i in line.strip("\n")] for line in file.readlines()]

def traverse(cave):
    costs = []
    for i in cave:
        costs.append([0 for j in cave[0]])

    heads = {(0, 0): 0}
    height = len(cave)
    width = len(cave[0])

    while True:
        new_heads = {}
        deleted_heads = set()

        for head in heads:
            i = head[0]
            j = head[1]
            head_is_useful = False
            if j + 1 < width and (costs[i][j + 1] > heads[head] + cave[i][j + 1] or costs[i][j + 1] == 0):
                head_is_useful = True
                if (i, j + 1) not in new_heads:
                    new_heads[(i, j + 1)] = heads[head] + cave[i][j + 1]
                else:
                    new_heads[(i, j + 1)] = min([new_heads[(i, j + 1)], heads[head] + cave[i][j + 1]])
            if i + 1 < height and (costs[i + 1][j] > heads[head] + cave[i + 1][j] or costs[i + 1][j] == 0):
                head_is_useful = True
                if (i + 1, j) not in new_heads:
                    new_heads[(i + 1, j)] = heads[head] + cave[i + 1][j]
                else:
                    new_heads[(i + 1, j)] = min([new_heads[(i + 1, j)], heads[head] + cave[i + 1][j]])
            if j - 1 >= 0 and (costs[i][j - 1] > heads[head] + cave[i][j - 1] or costs[i][j - 1] == 0):
                head_is_useful = True
                if (i, j - 1) not in new_heads:
                    new_heads[(i, j - 1)] = heads[head] + cave[i][j - 1]
                else:
                    new_heads[(i, j - 1)] = min([new_heads[(i, j - 1)], heads[head] + cave[i][j - 1]])
            if i - 1 >= 0 and (costs[i - 1][j] > heads[head] + cave[i - 1][j] or costs[i - 1][j] == 0):
                head_is_useful = True
                if (i - 1, j) not in new_heads:
                    new_heads[(i - 1, j)] = heads[head] + cave[i - 1][j]
                else:
                    new_heads[(i - 1, j)] = min([new_heads[(i - 1, j)], heads[head] + cave[i - 1][j]])

            if not head_is_useful:
                deleted_heads.add((i, j))

        for head in deleted_heads:
            if head in heads:
                heads.pop(head)

        for i, j in new_heads:
            heads[(i, j)] = new_heads[(i, j)]
            costs[i][j] = new_heads[(i, j)]

        if len(heads) == 0:
            return costs[height - 1][width - 1]

def quintificate(cave):
    height = len(cave)
    width = len(cave[0])
    fullcave = []
    fullrow = []
    for i in range(0, 5):
        for row in range(0, height):
            fullrow = []
            for j in range(0, 5):
                fullrow.extend([(x + i + j)%10 + int((x + i + j)/10) for x in cave[row][:]])
            fullcave.append(fullrow)
    return fullcave



# part one

cave = read_file("smalltestinput.txt")
answer = traverse(cave)
print(answer)

cave = read_file("testinput1.txt")
answer = traverse(cave)
print(answer)

cave = read_file("input.txt")
answer = traverse(cave)
print(answer)

# part two

cave = read_file("testinput1.txt")
fullcave = quintificate(cave)
answer = traverse(fullcave)
print(answer)

cave = read_file("testinput2.txt")
answer = traverse(cave)
print(answer)

cave = read_file("input.txt")
fullcave = quintificate(cave)
answer = traverse(fullcave)
print(answer)




















