import re
from functools import lru_cache

with open("input.txt", 'r') as reader:
    rules = {re.match(r'^\w+ \w+', rule).group(0): {content[1]: content[0] for content in re.findall(r'(\d+) (\w+ \w+)', rule)} for rule in reader.readlines()}

@lru_cache(None)
def can_reach(source, dest):
    return any(dest in rules[source] or can_reach(bag, dest) for bag in rules[source])

def bag_count(container):
    return sum(int(count) * (1 + bag_count(bag)) for bag,count in rules[container].items())

def part1():
    return sum(can_reach(rule, 'shiny gold') for rule in rules)

def part2():
    return bag_count('shiny gold')

print(part1())
print(part2())