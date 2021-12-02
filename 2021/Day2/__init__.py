import re


def init():
    lines = []

    file = open("Day2/input.txt", "r")
    for item in file:
        regex = re.compile('([a-zA-Z]+)\s([0-9]+)')
        rule = [x for x in regex.split(item.strip()) if len(x) > 0]
        lines.append(rule)

    for index, item in enumerate(lines):
        lines[index][1] = int(lines[index][1])

    return lines


# Part A
def part_a(lines):

    forward = 0
    depth = 0

    for item in lines:
        if item[0] == "forward":
            forward += item[1]
        if item[0] == "up":
            depth -= item[1]
        if item[0] == "down":
            depth += item[1]

    return forward*depth


# Part B
def part_b(lines):
    forward = 0
    depth = 0
    aim = 0

    for item in lines:
        if item[0] == "forward":
            forward += item[1]
            depth = depth + aim*item[1]
        if item[0] == "up":
            aim -= item[1]
        if item[0] == "down":
            aim += item[1]

    return forward*depth


def run():
    lines = init()
    print('Day 2\n', '- part A = ', part_a(lines), '\n', '- part B = ', part_b(lines), sep=' ')
