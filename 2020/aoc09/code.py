with open('input.txt', 'r') as reader:
    numbers = list(map(int, reader.readlines()))


def get_preamble(input, size):
    return input[:size]

def find_sum(input, preamble_size, sum):
    preamble = get_preamble(input, preamble_size)
    for i, i_val in enumerate(preamble):
        for j, j_val in enumerate(preamble):
            if i == j: continue
            if i_val + j_val == sum: return True
    return False

def find_invalid(input, preamble_size):
    return next(input[preamble_size + i] for i in range(len(numbers)) if not find_sum(numbers[i:], preamble_size, input[preamble_size + i]))

def part1():
    return find_invalid(numbers, 25)

def part2():
    invalid = part1()
    contiguous_set = []
    for i in numbers:
        contiguous_set.append(i)
        while sum(contiguous_set) > invalid:
            contiguous_set.pop(0)

        if  sum(contiguous_set) == invalid: return min(contiguous_set) + max(contiguous_set)

print(part1())
print(part2())