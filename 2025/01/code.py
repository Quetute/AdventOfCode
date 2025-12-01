with open("input.txt", "r") as reader:
    rotations = [line.strip() for line in reader.readlines()]


def part1():
    position = 50
    res = 0
    for r in rotations:
        position = (position + (1 if r[0] == "R" else -1) * int(r[1:])) % 100
        if position == 0:
            res += 1
    return res


def part2():
    dial = 50
    clicks = 0
    for rotation in rotations:
        dir = 1 if rotation[0] == "R" else -1
        dist = int(rotation[1:])

        if dist == 0:
            continue

        dial_calc = dial if dir > 0 else (100 - dial) % 100

        clicks += (dial_calc + dist) // 100
        dial = (dial + dir * dist) % 100

    return clicks


print(part1())
print(part2())
