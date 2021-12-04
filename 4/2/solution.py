
from math import floor
from functools import reduce


def read_file(filename):
    with open(filename) as file:
        contents = file.readlines()

    num_boards = int((len(contents) - 1) / 6)
    boards = []
    for i in range(0, num_boards):
        boards.append([])
        for j in range(0, 5):
                boards[i].append([0, 0, 0, 0, 0])

    line_number = 0
    for line in contents:
        line_number += 1
        if (line_number) < 3 or line == '\n':
            continue
        board_number = floor((line_number - 2) / 6)
        row_number = (line_number - 3) % 6
        boards[board_number][row_number][0] = int(line[0:2])
        boards[board_number][row_number][1] = int(line[3:5])
        boards[board_number][row_number][2] = int(line[6:8])
        boards[board_number][row_number][3] = int(line[9:11])
        boards[board_number][row_number][4] = int(line[12:14])

    return [int(i) for i in contents[0].strip('\n').split(',')], boards



filename = "../input.txt"

numbers, boards = read_file(filename)
winning_board_index = 0

for number in numbers:
    for board in range(0, len(boards)):
        for row in range(0, 5):
            for col in range(0, 5):
                if boards[board][row][col] == number:
                    boards[board][row][col] = -1

    bingo_row = [[-1, -1, -1, -1, -1] in board for board in boards]
    bingo_col = [[-1, -1, -1, -1, -1] in board for board in [list(map(list, zip(*board))) for board in boards]]
    bingo_any = [z[0] or z[1] for z in zip(bingo_row, bingo_col)]

    if bingo_any.count(False) == 1:
        next_number = numbers[numbers.index(number) + 1]
        last_board_index = bingo_any.index(False)
        for row in range(0, 5):
            for col in range(0, 5):
                if boards[last_board_index][row][col] == next_number:
                    boards[last_board_index][row][col] = -1
        print(numbers)
        print(next_number)
        print(boards[bingo_any.index(False)])
        print(next_number * reduce(lambda a, b: a + b, [element for row in boards[bingo_any.index(False)] for element in row if element > -1]))

    
