import re

with open('input.txt', 'r') as reader:
    lines = reader.readlines()
    i = 0 
    rules = {}
    while True:
        m = re.match(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', lines[i])
        if m is not None:
            rule_name = m.group(1)
            range1_min = int(m.group(2))
            range1_max = int(m.group(3))
            range2_min = int(m.group(4))
            range2_max = int(m.group(5))
            rules[rule_name] = (range(range1_min, range1_max + 1), range(range2_min, range2_max + 1))
        else:
            break
        i += 1
    #  skipping blank line and "your ticket:"
    i += 2
    your_ticket = list(map(int, lines[i].strip().split(',')))
    
    #  skipping blank line and "nearby ticket:"
    i += 3

    nearby_tickets = []
    while i < len(lines):
        nearby_tickets.append(list(map(int, lines[i].strip().split(','))))
        i += 1

def valid_value_for_rule(rule, v):
    return v in rule[0] or v in rule[1]

def invalid_values(ticket):
    return [v for v in ticket if not any(valid_value_for_rule(rule, v) for rule in rules.values())]

def part1():
    return sum([v for ticket in nearby_tickets for v in invalid_values(ticket)])

def part2():
    valid_tickets = [ticket for ticket in nearby_tickets if len(list(invalid_values(ticket))) == 0]
    possible_field_pos = {rule_name: set(range(len(rules))) for rule_name in rules}
    while any(len(possible_field_pos[p]) > 1 for p in possible_field_pos):
        for ticket in valid_tickets:
            for rule_name in rules:
                pos = set()
                for i in possible_field_pos[rule_name]:
                    if valid_value_for_rule(rules[rule_name], ticket[i]):
                        pos.add(i)
                    else:
                        inv = True
                if inv and len(pos) == 1:
                    for rule_name2 in possible_field_pos:
                        (e,) = pos
                        if e in possible_field_pos[rule_name2]:
                            possible_field_pos[rule_name2].remove(e)
                possible_field_pos[rule_name] = pos

    ret = 1
    for rule in possible_field_pos:
        if rule.startswith('departure'):
            (v,) = possible_field_pos[rule]
            ret *= your_ticket[v]

    return ret
print(part1())
print(part2())
