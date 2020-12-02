import re

with open('input.txt', 'r') as reader:
    lines = reader.readlines()


def part1():
    p = re.compile('(\d+)-(\d+)\s*(\w):\s*(\w*)')
    count = 0
    for line in lines:
        min, max, char, password = p.match(line).groups()
        char_count = password.count(char)
        if int(min) <= char_count and char_count <= int(max):
            count += 1
    return count


def part2():
    p = re.compile('(\d+)-(\d+)\s*(\w):\s*(\w*)')
    count = 0
    for line in lines:
        pos1, pos2, char, password = p.match(line).groups()
        char1 = password[int(pos1) - 1] if int(pos1) <= len(password) else ''
        char2 = password[int(pos2) - 1] if int(pos2) <= len(password) else ''
        if (char1 == char) ^ (char2 == char):
            count += 1
    return count


print(part1())
print(part2())
