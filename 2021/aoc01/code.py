with open('input.txt', 'r') as reader:
   depths = [int(line) for line in reader.readlines()]

def part1():
    return sum(1 if depths[i-1] < depths[i] else 0 for i in range(1, len(depths)))

def part2():
    return sum(1 if depths[i -1] < depths[i+2] else 0 for i in range(1, len(depths) - 2))

print(part1())
print(part2())
