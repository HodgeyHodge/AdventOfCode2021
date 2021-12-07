
#sum of distances is minimised at geometric median.

from statistics import median

def sum_distances(positions, position):
    d = 0
    for p in positions:
        d += abs(p - position)
    return d

filename = "input.txt"

with open(filename) as file:
    crab_positions = [int(i) for i in file.readline().split(',')]

crab_positions.sort()
print(crab_positions)
print(sum_distances(crab_positions, median(crab_positions)))



