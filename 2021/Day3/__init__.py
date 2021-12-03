from numpy import *


def init():
    matrix = []

    file = open("Day3/input.txt", "r")
    for item in file:
        matrix.append(list(item.strip()))

    return array(matrix)


# Part A
def part_a(matrix):
    gamma = ''
    epsilon = ''
    for i, row in enumerate(matrix.transpose()):
        count0 = 0
        count1 = 0
        for j, item in enumerate(row):
            if item == '0':
                count0 += 1
            if item == '1':
                count1 += 1
        gamma = gamma + '0' if count0 > count1 else gamma + '1'
        epsilon = epsilon + '0' if count0 < count1 else epsilon + '1'

    return int(gamma, 2) * int(epsilon, 2)


def inner(bits, oxygen):
    count0 = 0
    count1 = 0
    start_with_0 = []
    start_with_1 = []
    for i, item in enumerate(bits):
        if item == '0':
            count0 += 1
            start_with_0.append(i)
        if item == '1':
            count1 += 1
            start_with_1.append(i)

    if count0 > count1:
        return start_with_0 if oxygen else start_with_0
    else:
        return start_with_1 if oxygen else start_with_0


def oxygen(matrix):
    transposed = matrix.transpose()

    current_index_to_consider = list(range(len(matrix)))
    prev_matrix = transposed
    current_matrix = []
    index = 0

    while len(current_index_to_consider) > 1:
        current_index_to_consider = inner(prev_matrix[index], True)

        for i in current_index_to_consider:
            current_matrix.append(prev_matrix[:, i])

        prev_matrix = array(current_matrix).transpose()
        current_matrix = []
        index += 1

    oxygen = ''
    for x in prev_matrix.transpose()[0]:
        oxygen += x

    return int(oxygen, 2)


def co2(matrix):
    transposed = matrix.transpose()

    current_index_to_consider = list(range(len(matrix)))
    prev_matrix = transposed
    current_matrix = []
    index = 0

    while len(current_index_to_consider) > 1:
        current_index_to_consider = inner(prev_matrix[index], False)

        for i in current_index_to_consider:
            current_matrix.append(prev_matrix[:, i])

        prev_matrix = array(current_matrix).transpose()
        current_matrix = []
        index += 1

    co2 = ''
    for x in prev_matrix.transpose()[0]:
        co2 += x

    return int(co2, 2)


# Part B
def part_b(matrix):
    return oxygen(matrix) * co2(matrix)


def run():
    matrix = init()
    print('Day 3\n', '- part A = ', part_a(matrix), '\n', '- part B = ', part_b(matrix), sep=' ')
