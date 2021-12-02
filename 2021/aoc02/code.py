with open('input.txt', 'r') as reader:
   commands = [[line.split()[0], int(line.split()[1])] for line in reader.readlines()]

def part1():
    depth = 0
    horizontal = 0
    for cmd in commands:
        if cmd[0] == "forward":
            horizontal += cmd[1]
        elif cmd[0] == "up":
            depth -= cmd[1]
        elif cmd[0] == "down":
            depth += cmd[1]
    return depth * horizontal

def part2():
    depth = 0
    horizontal = 0
    aim = 0
    for cmd in commands:
        if cmd[0] == "forward":
            horizontal += cmd[1]
            depth += aim * cmd[1]
        elif cmd[0] == "up":
            aim -= cmd[1]
        elif cmd[0] == "down":
            aim += cmd[1]
    return depth * horizontal

print(part1())
print(part2())
