with open('input.txt', 'r') as reader:
    numbers = [int(s) for s in reader.readline().strip().split(',')]

def play(starting_numbers, stop):
    seen, say = {n: i + 1 for i, n in enumerate(starting_numbers)}, starting_numbers[-1]
    for t in range(len(numbers), stop):
        seen[say], say = t, 0 if say not in seen else t - seen[say]
    return say

def part1():
    return play(numbers, 2020)

def part2():
    return play(numbers, 30000000)

print(part1())
print(part2())