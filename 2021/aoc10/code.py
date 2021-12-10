from functools import reduce
from statistics import median

with open('input.txt', 'r') as reader:
    lines = reader.read().splitlines()
pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def part1():
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    sum  = 0
    for line in lines:
        queue = []
        for char in line:
            if char in pairs:
                queue.append(char)
            elif len(queue) == 0 or pairs[queue.pop()] != char:
                    sum += scores[char]
                    break
    return sum

def part2():
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    sums  = []
    for line in lines:
        queue = []
        corrupted = False
        for char in line:
            if char in pairs:
                queue.append(char)
            elif len(queue) == 0 or pairs[queue.pop()] != char:
                corrupted = True
                break
        if corrupted:
            continue
        sum = reduce(lambda s, char: s * 5 + scores[pairs[char]], reversed(queue), 0)
        sums.append(sum)
    sums.sort()
    return median(sums)


print(part1())
print(part2())
