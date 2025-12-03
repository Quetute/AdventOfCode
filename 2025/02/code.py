import itertools
from math import ceil
import re


with open("input.txt", "r") as reader:
    line = reader.readline().strip()
    ranges = [r.split("-") for r in line.split(",")]
    id_ranges = [(int(a), int(b)) for [a, b] in ranges]


def part1():
    total = 0
    for r_min, r_max in id_ranges:
        curr_str = str(r_min)
        if len(curr_str) % 2 == 1:
            curr_str = str(10 ** len(curr_str))
        mid = len(curr_str) // 2
        left_half, right_half = curr_str[:mid], curr_str[mid:]
        if int(left_half) < int(right_half):
            left_half = str(int(left_half) + 1)
        while (curr := int(f"{left_half}{left_half}")) <= r_max:
            total += curr
            left_half = str(int(left_half) + 1)

    return total


def part2():
    total = 0

    def is_repeat(i: int) -> bool:
        i_str = str(i)
        total_length = len(i_str)
        for size in range(1, total_length):
            if (
                total_length % size == 0
                and len(set(itertools.batched(i_str, size))) == 1
            ):
                return True
        return False

    # seen on reddit, not bad
    reg = re.compile(r"(\d+)\1+")

    def is_repeat2(i: int) -> bool:
        return re.match(reg, str(i)) is not None

    for r_min, r_max in id_ranges:
        # brute force :(
        for i in range(r_min, r_max + 1):
            if is_repeat(i):
                total += i

    return total


# print(part1())
print(part2())
