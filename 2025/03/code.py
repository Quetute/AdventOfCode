with open("input.txt", "r") as reader:
    banks = reader.read().splitlines()


def part1():
    total = 0
    for bank in banks:
        a, b = 0, 0
        for v in bank:
            if a < b:
                a, b = b, int(v)
            else:
                b = max(b, int(v))
            if a == 9 and b == 9:
                break
        total += 10 * a + b
    return total


def part2():
    size = 12
    total = 0
    for bank in banks:
        joltages = [0] * size
        for v in bank:
            joltages += [int(v)]
            for i in range(size):
                if joltages[i] < joltages[i + 1]:
                    joltages = joltages[:i] + joltages[i + 1 :]
                    break
            joltages = joltages[:size]

        total += int("".join(map(str, joltages)))
    return total


print(part1())
print(part2())
