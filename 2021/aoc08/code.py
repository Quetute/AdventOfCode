with open('input.txt', 'r') as reader:
    input = []
    for line in reader.read().splitlines():
        split = line.split('|')
        input.append((split[0].split(), split[1].split()))

def part1():
    return len([digit for val in input for digit in val[1] if len(digit) in [2, 3, 4 ,7]])


def part2():
    pass

print(part1())
print(part2())