with open('input.txt', 'r') as reader:
   input = [line for line in reader.read().splitlines()]

def part1(numbers):
    length = len(numbers[0])
    sums = [0] * length
    for number in numbers:
        for i in range(length):
            sums[i] += int(number[i])
    gamma = [1 if v > len(numbers) / 2 else 0 for v in sums]
    gammaV = bin_arr_to_int(gamma)
    return gammaV * (gammaV ^ int("".join([str(1)]*length), 2))

def part2(numbers):
    idx = range(len(numbers))
    current = 0
    while(len(idx) > 1):
        sum_current = sum([int(numbers[i][current]) for i in idx])
        most_common = "1" if sum_current >= len(idx)/ 2 else "0"
        idx = list(filter(lambda i: numbers[i][current] == most_common, idx))
        current += 1
    oxygen_generator_rating = bin_arr_to_int(numbers[idx[0]])

    idx = range(len(numbers))
    current = 0
    while(len(idx) > 1):
        sum_current = sum([int(numbers[i][current]) for i in idx])
        least_common = "1" if sum_current < len(idx)/ 2 else "0"
        idx = list(filter(lambda i: numbers[i][current] == least_common, idx))
        current += 1
    CO2_scrubber_rating = bin_arr_to_int(numbers[idx[0]])
    return oxygen_generator_rating * CO2_scrubber_rating


def bin_arr_to_int(binary):
    return int("".join([str(v) for v in binary]), 2)

print(part1(input))
print(part2(input))
