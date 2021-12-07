import re
from collections import Counter
with open('input.txt', 'r') as reader:
    lines = [list(map(lambda v: list(map(int, v.split(","))),re.findall("\d+,\d+",line))) for line in reader.read().splitlines()]


def part1():
    vent_count = Counter()
    for line in lines:
        x1, y1 ,x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    vent_count[(x,y)] += 1
    return len([v for (v, count) in vent_count.items() if count > 1])

def part2():
    vent_count = Counter()
    for line in lines:
        x1, y1 ,x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        dx = 1 if x2 > x1 else 0 if x2 == x1 else -1 
        dy = 1 if y2 > y1 else 0 if y2 == y1 else -1 
        vent_count[(x1, y1)] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx 
            y1 += dy
            vent_count[(x1, y1)] += 1
    return len([v for (v, count) in vent_count.items() if count > 1])

print(part1())
print(part2())
