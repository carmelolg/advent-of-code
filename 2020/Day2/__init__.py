import re


def init():
    lines = []
    file = open("Day2/input.txt", "r")
    for item in file:
        lines.append(item)

    return lines


# Part A
def part_a(lines):
    count_a = 0
    for item in lines:
        regex = re.compile('([0-9]+)-([0-9]+)\s([a-zA-Z]):\s([a-zA-Z]+)')
        rule = [x for x in regex.split(item.strip()) if len(x) > 0]
        password = rule[3]
        lower_bound = rule[0]
        upper_bound = rule[1]
        char = rule[2]
        if int(lower_bound) <= password.count(char) <= int(upper_bound):
            count_a = count_a + 1;

    return count_a


# Part B
def part_b(lines):
    count_b = 0
    for item in lines:
        regex = re.compile('([0-9]+)-([0-9]+)\s([a-zA-Z]):\s([a-zA-Z]+)')
        rule = [x for x in regex.split(item.strip()) if len(x) > 0]
        password = rule[3]
        lower_bound = int(rule[0])
        upper_bound = int(rule[1])
        char = rule[2]
        if (password[lower_bound - 1] == char) != (password[upper_bound - 1] == char):
            count_b = count_b + 1

    return count_b


def run():
    lines = init()
    print('Day 2\n', '- part A = ', part_a(lines), '\n', '- part B = ', part_b(lines), sep=' ')
