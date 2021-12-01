numbers = []


# Part A
def part_a():
    file = open("Day1/input.txt", "r")
    for item in file:
        numbers.append(int(item))

    for item in numbers:
        for item_2 in numbers:
            if item != item_2 and item + item_2 == 2020:
                return item * item_2

    return -1


# Part B
def part_b():
    file = open("Day1/input.txt", "r")
    for item in file:
        numbers.append(int(item))

    for i, item in enumerate(numbers):
        for j, item_2 in enumerate(numbers[i:len(numbers)]):
            if item + item_2 >= 2020:
                continue
            else:
                for item_3 in numbers[j:len(numbers)]:
                    if item + item_2 + item_3 == 2020:
                        return item * item_2 * item_3

    return -1


def run():
    print('Day 1\n', '- part A = ', part_a(), '\n', '- part B = ', part_b(), sep=' ')
