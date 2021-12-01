def init():
    lines = []
    file = open("Day1/input.txt", "r")
    for item in file:
        lines.append(int(item))

    return lines


# Part A
def part_a(lines):
    count_a = 0
    for i, item in enumerate(lines):
        if i + 1 == len(lines):
            break
        if lines[i + 1] > lines[i]:
            count_a = count_a + 1

    return count_a


# Part B
def part_b(lines):
    count_b = 0
    group = []
    for i in range(len(lines)):

        if i + 1 == len(lines) or i + 2 == len(lines):
            break

        subgroup = lines[i:i + 3]
        group.append(sum(subgroup))

    for k, item in enumerate(group):
        if k + 1 == len(group):
            break
        if group[k + 1] > group[k]:
            count_b = count_b + 1

    return count_b


def run():
    lines = init()
    print('Day 1\n', '- part A = ', part_a(lines), '\n', '- part B = ', part_b(lines), sep=' ')
