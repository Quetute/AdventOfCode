from collections import Counter

with open('input.txt', 'r') as reader:
    fishs = list(map(lambda v: int(v), reader.readline().split(",")))

def part1():
    curr_fishs = fishs
    for day in range(80):
        new_fishs = []
        for fish in curr_fishs:
            if fish == 0:
                new_fishs.append(6)
                new_fishs.append(8)
            else:
                new_fishs.append(fish - 1)
        curr_fishs = new_fishs
    return len(curr_fishs)

def part2():
    fish_count = Counter(fishs)
    for day in range(256):
        new_fish_count = Counter()
        for (fish, count) in fish_count.items():
            if fish == 0:
                new_fish_count[6] += count
                new_fish_count[8] += count
            else:
                new_fish_count[fish - 1] += count
        fish_count = new_fish_count
    return sum([count for (v, count) in fish_count.items()])

print(fishs)

print(part1())
print(part2())
