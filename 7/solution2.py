
#this time let's do some maths: function is minimised where derivative is zero.

from math import copysign

def sum_distances(positions, position):
    d = 0
    for p in positions:
        d += 0.5 * abs(p - position) + 0.5 * (p - position)**2
    return d

filename = "input.txt"

with open(filename) as file:
    crab_positions = [int(i) for i in file.readline().split(',')]

S = sum(crab_positions)
i = len(crab_positions)

def minimiser(p):
    return 2 * (i * p - S) + sum([copysign(1, p - x) for x in crab_positions]) 

#a bit of manual interval bisection later :^)

print(minimiser(471))
print(minimiser(472))

print(sum_distances(crab_positions, 471))
print(sum_distances(crab_positions, 472))



