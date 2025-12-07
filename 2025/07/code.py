import copy
from csv import Error
from functools import lru_cache


with open("input.txt", "r") as reader:
    lines = [list(line) for line in reader.read().splitlines()]


def part1():
    lines_copy = copy.deepcopy(lines)
    start = lines_copy[0].index("S")
    width = len(lines_copy[0])
    height = len(lines_copy)
    split = 0
    beams: list[tuple[int, int]] = []
    beams.append((1, start))
    while len(beams) > 0:
        pos = beams.pop()
        if lines_copy[pos[0]][pos[1]] == "|":
            continue
        lines_copy[pos[0]][pos[1]] = "|"
        if pos[0] >= height - 1:
            continue
        match lines_copy[pos[0] + 1][pos[1]]:
            case ".":
                beams.append((pos[0] + 1, pos[1]))
            case "^":
                split += 1
                if pos[1] > 0:
                    beams.append((pos[0] + 1, pos[1] - 1))
                if pos[1] < width - 1:
                    beams.append((pos[0] + 1, pos[1] + 1))
            case _:
                pass

    return split


def part2():
    start = lines[0].index("S")
    width = len(lines[0])
    height = len(lines)

    @lru_cache
    def get_timelines(y: int, x: int) -> int:
        val = lines[y][x]
        match val:
            case ".":
                return 1 if y >= height - 1 else get_timelines(y + 1, x)
            case "^":
                tot = 0
                if x > 0:
                    tot += get_timelines(y, x - 1)
                if x < width - 1:
                    tot += get_timelines(y, x + 1)
                return tot
            case _:
                raise Error("parsing error")

    return get_timelines(1, start)


print(part1())
print(part2())
