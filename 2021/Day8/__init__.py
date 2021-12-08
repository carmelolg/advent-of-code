from numpy import *
import re

digits_utils = dict()
digits_utils['2'] = [1]
digits_utils['3'] = [7]
digits_utils['4'] = [4]
digits_utils['5'] = [2, 3, 5]
digits_utils['6'] = [0, 6, 9]
digits_utils['7'] = [8]


def init():
    file = open("Day8/input.txt", "r")
    regex = re.compile('(.*)\|(.*)')
    result = []
    for line in file:
        if len(line.strip()) > 0:
            groups = [x for x in regex.split(line.strip()) if len(x) > 0]
            result.append([groups[0].split(), groups[1].split()])

    return result


def get_fixed_digits():
    fixed_digits = []
    for key in digits_utils.keys():
        if len(digits_utils[key]) == 1:
            fixed_digits.append(int(key))

    return fixed_digits


# Part A
def part_a(digits):
    count = 0
    fixed_digits = get_fixed_digits()
    for row in digits:
        for digit in row[1]:
            if len(digit) in fixed_digits:
                count += 1
    return count


# Part B
def part_b(digits):
    map = [set()] * 10
    total = 0
    for row in digits:
        for input_digit in row[0]:
            if len(input_digit) == 2:
                map[1] = set(input_digit)
            elif len(input_digit) == 4:
                map[4] = set(input_digit)
            elif len(input_digit) == 3:
                map[7] = set(input_digit)
            elif len(input_digit) == 7:
                map[8] = set(input_digit)

        for input_digit in row[0]:
            if len(input_digit) == 5:
                if len(map[1] - set(input_digit)) == 0:
                    map[3] = set(input_digit)
                elif len(set(input_digit) - map[4]) == 2:
                    map[5] = set(input_digit)
                elif len(set(input_digit) - map[4]) == 3:
                    map[2] = set(input_digit)

        for input_digit in row[0]:
            if len(input_digit) == 6:
                if len(map[1] - set(input_digit)) == 1:
                    map[6] = set(input_digit)
                elif len(map[5] - set(input_digit)) == 0:
                    map[9] = set(input_digit)
                else:
                    map[0] = set(input_digit)

        final_number = ''
        for digit in row[1]:
            final_number += str(map.index(set(digit.strip())))

        total += int(final_number)

    return total


def run():
    digits = init()
    a = part_a(digits)
    b = part_b(digits)
    print('Day 8\n', '- part A = ', a, '\n', '- part B = ', b, sep=' ')
