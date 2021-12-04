from numpy import *

boards = []
numbers = []


def init():
    global boards
    global numbers

    _boards = []
    file = open("Day4/input.txt", "r")
    _numbers = list(map(int, file.readline().strip().split(",")))
    board = []
    for row in file:
        if not bool(row.strip()):
            if len(board) > 0:
                _boards.append(board)
            board = []
        else:
            board.append(list(map(int, row.strip().split())))

    boards = _boards
    numbers = _numbers


def is_the_winner(board, numbers_out):
    for row in board:
        if set(row).issubset(numbers_out):
            return True

    for row in array(board).transpose():
        if set(row).issubset(numbers_out):
            return True

    return False


def get_the_winner(sublist_numbers):
    for i, board in enumerate(boards):
        if is_the_winner(board, sublist_numbers):
            return {"index": i, "board": board}

    return None


def take_not_called_numbers(board, sublist_numbers):
    not_called_numbers = []
    for row in board:
        for number in row:
            if number in sublist_numbers:
                pass
            else:
                not_called_numbers.append(number)

    return not_called_numbers


# Part A
def part_a():
    index = 1
    while True:
        winner = get_the_winner(numbers[:index])
        if winner is not None:
            return sum(take_not_called_numbers(winner["board"], numbers[:index])) * numbers[index - 1]

        else:
            index += 1


def last_winner():
    for board in boards:
        if is_the_winner(board, numbers):
            return board

    return None


# Part B
def part_b():
    index = 1
    while True:
        winner = get_the_winner(numbers[:index])

        if winner is not None and len(boards) == 1:
            return sum(take_not_called_numbers(winner["board"], numbers[:index])) * numbers[index - 1]
        elif winner is not None:
            boards.pop(winner["index"])
        else:
            index += 1


def run():
    init()
    a = part_a()
    b = part_b()
    print('Day 4\n', '- part A = ', a, '\n', '- part B = ', b, sep=' ')
