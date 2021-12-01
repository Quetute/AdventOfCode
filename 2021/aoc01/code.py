with open('input.txt', 'r') as reader:
   depths = [int(line) for line in reader.readlines()]

def part1():
    count = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            count += 1
    return count

def part2():
    count = 0
    for i in range(1, len(depths) - 2):
        if depths[i-1] < depths[i+2]:
            count += 1
    return count

print(part1())
print(part2())
