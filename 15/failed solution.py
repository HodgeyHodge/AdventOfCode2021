
def read_file(filename):
    with open(filename) as file:
        return [line.strip("\n") for line in file.readlines()]

def iterate(paths):
    """
    For each path in collection, return three new paths, except that:
    a) Paths cannot go adjacent to their own tails.
    b) Of paths ending at a given point, destroy all but the lowest risk one.
    """
    new_paths = []
    for path in paths:
        #print('doing path:', path)
        i = path[0][-1][0]
        j = path[0][-1][1]
        #print('head:', i, j)
        if i + 1 < height and not any(x in path[0][0:-1] for x in [(i, j), (i + 1, j + 1), (i + 1, j - 1), (i + 2, j)]):
            #print('step south:', i + 1, j)
            new_route = path[0][:]
            new_route.append((i + 1, j))
            #print(new_route)
            new_risk = path[1] + int(cave[i + 1][j])
            #print(new_risk)
            new_paths.append((new_route, new_risk))
        if j + 1 < width and not any(x in path[0][0:-1] for x in [(i, j), (i - 1, j + 1), (i + 1, j + 1), (i, j + 2)]):
            #print('step east:', i, j + 1)
            new_route = path[0][:]
            new_route.append((i, j + 1))
            #print(new_route)
            new_risk = path[1] + int(cave[i][j + 1])
            #print(new_risk)
            new_paths.append((new_route, new_risk))
        if i - 1 >= 0 and not any(x in path[0][0:-1] for x in [(i, j), (i - 1, j + 1), (i - 1, j - 1), (i - 2, j)]):
            #print('step north:', i - 1, j)
            new_route = path[0][:]
            new_route.append((i - 1, j))
            #print(new_route)
            new_risk = path[1] + int(cave[i - 1][j])
            #print(new_risk)
            new_paths.append((new_route, new_risk))
        if j - 1 >= 0 and not any(x in path[0][0:-1] for x in [(i, j), (i - 1, j - 1), (i + 1, j - 1), (i, j - 2)]):
            #print('step east:', i, j - 1)
            new_route = path[0][:]
            new_route.append((i, j - 1))
            #print(new_route)
            new_risk = path[1] + int(cave[i][j - 1])
            #print(new_risk)
            new_paths.append((new_route, new_risk))
    return new_paths

def deduplicate(paths):
    #print('deduplicating.')
    good_paths = []
    for path in paths:
        #print('deduplicating on path:', path)
        cheaper_paths = [overlapping_path for overlapping_path in paths if (path[0][-1] in overlapping_path[0]) and path[1] > overlapping_path[1]]
        #print('cheaper paths:', cheaper_paths)
        if len(cheaper_paths) == 0:
            good_paths.append(path)
    return good_paths

def part_one(paths):
    completed_paths = []
    #print(paths)
    while True:
        paths = iterate(paths)
        paths = deduplicate(paths)
        if len(completed_paths) > 0:
            paths = [path for path in paths if path[1] <= min([x[1] for x in completed_paths])]
        for path in paths:
            if path[0][-1] == (height - 1, width - 1):
                completed_paths.append(path)
        if len(paths) == 0:
            return completed_paths



cave = read_file("testinput1.txt")
height =len(cave)
width = len(cave[0])
paths = [([(0, 0)], 0)]
completed_paths = part_one(paths)
for p in completed_paths:
    print(p)

# add logging and metrics to see wtf is going on!
