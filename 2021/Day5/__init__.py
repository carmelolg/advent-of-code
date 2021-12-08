from numpy import *
import re


def init_a():
    file = open("Day5/input.txt", "r")
    ocean = full((1000, 1000), 0)
    for line in file:
        regex = re.compile('([0-9]+),([0-9]+)\s->\s([0-9]+),([0-9]+)')
        # col1, row1, col2, row2
        coordinates = [int(x) for x in regex.split(line.strip()) if len(x) > 0]
        row1 = coordinates[1]
        col1 = coordinates[0]
        row2 = coordinates[3]
        col2 = coordinates[2]

        if row1 == row2:
            for col in range(col1, col2 - 1 if col2 < col1 else col2 + 1, -1 if col2 < col1 else 1):
                ocean[row1][col] = 1 if ocean[row1][col] == 0 else ocean[row1][col] + 1
        if col1 == col2:
            for row in range(row1, row2 - 1 if row2 < row1 else row2 + 1, -1 if row2 < row1 else 1):
                ocean[row][col1] = 1 if ocean[row][col1] == 0 else ocean[row][col1] + 1

    return ocean


def set_diagonal_points(matrix, row1, col1, row2, col2):
    if row1 > row2:
        row1, col1, row2, col2 = row2, col2, row1, col1

    slope = (col2 - col1) // (row2 - row1)
    for i, j in zip(range(row1, row2 - 1 if row2 < row1 else row2 + 1),
                    range(col1, col2 - 1 if col2 < col1 else col2 + 1, slope)):
        matrix[i][j] += 1

    return matrix


def init_b():
    file = open("Day5/input.txt", "r")
    ocean = full((1000, 1000), 0)
    for line in file:
        regex = re.compile('([0-9]+),([0-9]+)\s->\s([0-9]+),([0-9]+)')
        # col1, row1, col2, row2
        coordinates = [int(x) for x in regex.split(line.strip()) if len(x) > 0]
        row1 = coordinates[1]
        col1 = coordinates[0]
        row2 = coordinates[3]
        col2 = coordinates[2]

        if row1 == row2:
            for col in range(col1, col2 - 1 if col2 < col1 else col2 + 1, -1 if col2 < col1 else 1):
                ocean[row1][col] = 1 if ocean[row1][col] == 0 else ocean[row1][col] + 1
        elif col1 == col2:
            for row in range(row1, row2 - 1 if row2 < row1 else row2 + 1, -1 if row2 < row1 else 1):
                ocean[row][col1] = 1 if ocean[row][col1] == 0 else ocean[row][col1] + 1
        else:
            ocean = set_diagonal_points(ocean, row1, col1, row2, col2)

    return ocean


# Part A
def part_a(ocean):
    return count_nonzero(ocean >= 2)


# Part B
def part_b(ocean):
    return count_nonzero(ocean >= 2)


def run():
    ocean_a = init_a()
    ocean_b = init_b()
    a = part_a(ocean_a)
    b = part_b(ocean_b)
    print('Day 5\n', '- part A = ', a, '\n', '- part B = ', b, sep=' ')
