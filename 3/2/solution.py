
def find_filter(l, pos, inverse):
    length = len(l)
    width = len(l[0])
    bitsum = 0
    for string in l:
        bitsum += int(string[pos])
    if inverse:
        return int(bitsum < length/2)
    else:
        return int(bitsum >= length/2)

def reduce_list(l, f, pos):
    return [i for i in l if int(i[pos]) == f]

def find_rating(l, inverse):
    for pos in range(0, len(l[0])):
        f = find_filter(l, pos, inverse)
        l = reduce_list(l, f, pos)
        if len(l) == 1:
            break
    return l
        


filename = "../input.txt"

with open(filename) as file:
    lines = [line.strip('\n') for line in file.readlines()]

print(find_rating(lines, False))
print(find_rating(lines, True))





