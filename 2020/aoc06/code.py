with open("input.txt", 'r') as reader:
    groups = reader.read().split('\n\n')

def part1():
    return sum(len(set.union(*map(set, group.splitlines()))) for group in groups)

def part2():
    return sum(len(set.intersection(*map(set, group.splitlines()))) for group in groups)

print(part1())
print(part2())