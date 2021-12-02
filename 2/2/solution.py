file = open("input.txt", "r")

horizontal = 0
depth = 0
aim = 0

#down X increases your aim by X units.
#up X decreases your aim by X units.
#forward X does two things:
#    It increases your horizontal position by X units.
#    It increases your depth by your aim multiplied by X.


for line in file:
    if (line.startswith('forward ')):
        horizontal += int(line[8:])
        depth += aim * int(line[8:])
    elif (line.startswith('down ')):
        aim += int(line[5:])
    elif (line.startswith('up ')):
        aim -= int(line[3:])

print(horizontal * depth)

file.close()
