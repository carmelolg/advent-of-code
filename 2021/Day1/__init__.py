numbers = []


# Part A
def part_a():
    file = open("Day1/01_input.txt", "r")
    for item in file:
        numbers.append(int(item))

    count_a = 0
    for i, item in enumerate(numbers):
        if i + 1 == len(numbers):
            break
        if numbers[i + 1] > numbers[i]:
            count_a = count_a + 1

    return count_a


# Part B
def part_b():
    count_b = 0
    group = []
    for i in range(len(numbers)):

        if i + 1 == len(numbers) or i + 2 == len(numbers):
            break

        subgroup = numbers[i:i + 3]
        group.append(sum(subgroup))

    for k, item in enumerate(group):
        if k + 1 == len(group):
            break
        if group[k + 1] > group[k]:
            count_b = count_b + 1

    return count_b


def run():
    print('Day 1\n', '- part A = ', part_a(), '\n', '- part B = ', part_b(), sep=' ')
