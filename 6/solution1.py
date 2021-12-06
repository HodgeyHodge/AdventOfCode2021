
#the naive way to proceed: modelling as written
#this works for part 1 but part 2 runs into performance issues

def iterate_list(fish_list):
    new_list = []
    for fish in fish_list:
        if fish > 0:
            new_list.append(fish - 1)
        elif fish == 0:
            new_list.append(6)
            new_list.append(8)
    return new_list

def iterate_list_repeatedly(fish_list, days):
    for i in range(0, days):
        fish_list = iterate_list(fish_list)
    return len(fish_list)

filename = "testinput.txt"

with open(filename) as file:
    fish_list = [int(i) for i in file.readline().split(',')]

print(iterate_list_repeatedly(fish_list, 80))
