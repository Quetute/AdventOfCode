import re

def parse(line):
    m = re.match(r'^(nop|acc|jmp) ((?:-|\+)\d+)$', line)
    return [m.group(1), int(m.group(2))]

with open('input.txt', 'r') as reader: 
    instructions = [parse(line) for line in reader.readlines()]

def run(insts):
    seen = set()
    curr = 0
    acc = 0
    while curr not in seen and curr < len(insts):
        seen.add(curr)
        curr, acc = {
            'nop': lambda curr, acc: (curr + 1, acc),
            'acc': lambda curr, acc: (curr + 1, acc + insts[curr][1]),
            'jmp': lambda curr, acc: (curr + insts[curr][1], acc)
        }[insts[curr][0]](curr, acc)
    return (curr >= len(insts), acc)

def part1():
    return run(instructions)[1]

CORRUPT_MAP = {
    'jmp': 'nop',
    'nop': 'jmp'
}

def part2():
    for idx in range(0, len(instructions)):
        corrupt_inst = instructions[idx][0]
        if corrupt_inst in CORRUPT_MAP:
            instructions[idx][0] = CORRUPT_MAP[corrupt_inst]
            finish, acc = run(instructions)
            if finish:
                return acc
            instructions[idx][0] = corrupt_inst        

print(part1())
print(part2())