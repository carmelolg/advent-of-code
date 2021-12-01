from numpy import *


def init():
    lines = []
    file = open("Day3/input.txt", "r")
    for item in file:
        line = list("".join(item.strip() * 500))
        lines.append(line)

    return array(lines)


# Part A
def part_a(morphology):
    current_position = {}
    current_position['x'] = 0
    current_position['y'] = 0
    count = 0

    while current_position['x'] < len(morphology):
        column = morphology[current_position['x']]
        if current_position['y'] < len(column) and morphology[current_position['x']][current_position['y']] == '#':
            count += 1

        current_position['x'] = current_position['x'] + 1
        current_position['y'] = current_position['y'] + 3

    return count


# Part B
def part_b(morphology):
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]];

    result = 1
    for slope in slopes:
        x_slope = slope[0]
        y_slope = slope[1]

        current_position = {}
        current_position['x'] = 0
        current_position['y'] = 0

        count = 0
        while current_position['x'] < len(morphology):
            column = morphology[current_position['x']]
            if current_position['y'] < len(column) and morphology[current_position['x']][current_position['y']] == '#':
                count += 1

            current_position['x'] = current_position['x'] + x_slope
            current_position['y'] = current_position['y'] + y_slope

        result *= count

    return result


def run():
    lines = init()
    print('Day 3\n', '- part A = ', part_a(lines), '\n', '- part B = ', part_b(lines), sep=' ')
