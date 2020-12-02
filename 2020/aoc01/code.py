with open('input.txt', 'r') as reader:
    expenses = set([int(line) for line in reader.readlines()])


def part1():
    for expense in expenses:
        entry = 2020 - expense
        if entry in expenses:
            return entry * expense


def part2():
    for expense in expenses:
        for expense2 in expenses:
            entry = 2020 - expense - expense2
            if entry in expenses:
                return entry * expense * expense2


print(part1())
print(part2())
