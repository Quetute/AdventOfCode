from statistics import median, mean
from math import floor, ceil

with open('input.txt', 'r') as reader:
    crabs = list(map(lambda v: int(v), reader.readline().split(",")))

def part1():
    crab_median = median(crabs)
    return sum([abs(x - crab_median) for x in crabs])

def part2():
    crab_mean = mean(crabs)
    fuel = lambda x: x * (x + 1) / 2
    return min(sum([fuel(abs(x - ceil(crab_mean))) for x in crabs]), sum([fuel(abs(x - floor(crab_mean))) for x in crabs]))

print(part1())
print(part2())
