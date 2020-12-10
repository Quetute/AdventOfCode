from functools import lru_cache

with open('input.txt', 'r') as reader:
    joltages = sorted(map(int,reader.readlines()))
    joltages = [0] + joltages + [max(joltages) + 3]

def part1():
    count1, count3 = 0, 0
    for i in range(len(joltages) - 1):
        diff = joltages[i+1] - joltages[i]
        if diff == 1: count1 += 1
        if diff == 3: count3 += 1

    return count1 * count3

@lru_cache(None)
def arrangments(idx):
    return sum(arrangments(idx - i) for i in range(1, min(4, idx+1)) if joltages[idx] - joltages[idx - i] <= 3) if idx > 0 else 1
    
def part2():
    return arrangments(len(joltages) - 1)

print(part1())
print(part2())