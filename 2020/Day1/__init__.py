def init():
    lines = []
    file = open("Day1/input.txt", "r")
    for item in file:
        lines.append(int(item))

    return lines


# Part A
def part_a(lines):
    for item in lines:
        for item_2 in lines:
            if item != item_2 and item + item_2 == 2020:
                return item * item_2

    return -1


# Part B
def part_b(lines):
    for i, item in enumerate(lines):
        for j, item_2 in enumerate(lines[i:len(lines)]):
            if item + item_2 >= 2020:
                continue
            else:
                for item_3 in lines[j:len(lines)]:
                    if item + item_2 + item_3 == 2020:
                        return item * item_2 * item_3

    return -1


def run():
    lines = init()
    print('Day 1\n', '- part A = ', part_a(lines), '\n', '- part B = ', part_b(lines), sep=' ')
