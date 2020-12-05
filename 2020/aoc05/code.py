with open('input.txt', 'r') as reader:
    passes = reader.readlines()

id = lambda row, column: row * 8 + column
lower_half = lambda min, max: (min, min + int((max - min) / 2))
upper_half = lambda min, max: (1 + min + int((max - min) / 2), max)

HALFS = {
    'F': lower_half,
    'B': upper_half,
    'L': lower_half,
    'R': upper_half
}

def position(min, max, partition):
    for char in partition:
        min, max = HALFS[char](min, max)
    return min

seat = lambda partition: (position(0, 127, partition[:7]), position(0, 7, partition[7:10]))
ids = [id(*seat(partition)) for partition in passes]

def part1():
    return max(ids)

def part2():
    sort = sorted(ids)
    return next(id - 1 for idx, id  in enumerate(sort) if id != sort[0] + idx)

print(part1())
print(part2())