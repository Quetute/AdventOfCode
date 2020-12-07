import re
from functools import lru_cache

def parse_rule(rule):
    bag = re.match(r'^\w+ \w+', rule).group(0)
    contents = re.findall(r'(\d+) (\w+ \w+)', rule)
    return (bag, {content[1]: content[0] for content in contents})

with open("input.txt", 'r') as reader:
    rules = dict(map(parse_rule, reader.readlines()))

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