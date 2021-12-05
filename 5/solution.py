
from math import copysign

def vent_locations(file, include_diagonals):
    vent_dict = {}
    
    for line in file:
        segment = [[int(j) for j in i] for i in [coords.split(',') for coords in line.strip('\n').split(' -> ')]]

        #horizontal
        if segment[0][0] == segment[1][0] and segment[0][1] != segment[1][1]:
            start = min(segment[0][1], segment[1][1])
            end = max(segment[0][1], segment[1][1])
            for pos in range(start, end + 1):
                coord = (segment[0][0], pos)
                if coord not in vent_dict:
                    vent_dict[coord] = 1
                else:
                    vent_dict[coord] += 1

        #vertical
        elif segment[0][0] != segment[1][0] and segment[0][1] == segment[1][1]:
            start = min(segment[0][0], segment[1][0])
            end = max(segment[0][0], segment[1][0])
            for pos in range(start, end + 1):
                coord = (pos, segment[0][1])
                if coord not in vent_dict:
                    vent_dict[coord] = 1
                else:
                    vent_dict[coord] += 1

        #diagonal
        elif include_diagonals:
            for i in range(0, abs(segment[1][0] - segment[0][0]) + 1):
                coord = (((segment[0][0] + i * int(copysign(1, segment[1][0] - segment[0][0]))), segment[0][1] + i * int(copysign(1, segment[1][1] - segment[0][1]))))
                if coord not in vent_dict:
                    vent_dict[coord] = 1
                else:
                    vent_dict[coord] += 1

    return vent_dict

filename = "input.txt"

with open(filename) as file:
    print(sum(value > 1 for value in vent_locations(file, False).values()))
with open(filename) as file:
    print(sum(value > 1 for value in vent_locations(file, True).values()))



