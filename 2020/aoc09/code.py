with open('input.txt', 'r') as reader:
    numbers = list(map(int, reader.readlines()))

valid = lambda preamble, sum: any(preamble[i] + preamble[j] == sum for i in range(len(preamble)) for j in range(i+1, len(preamble)))
find_invalid = lambda input, preamble_size: next(input[preamble_size + i] for i in range(len(numbers)) if not valid(numbers[i:i+preamble_size], input[preamble_size + i]))

def part1():
    return find_invalid(numbers, 25)

def part2():
    invalid = part1()
    contiguous_set = []
    for i in numbers:
        contiguous_set.append(i)
        while sum(contiguous_set) > invalid: contiguous_set.pop(0)
        if sum(contiguous_set) == invalid: return min(contiguous_set) + max(contiguous_set)

print(part1())
print(part2())