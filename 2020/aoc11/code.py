with open('input.txt', 'r') as reader:
    layout = [[c for c in line.strip()] for line in reader.readlines()]
    x_max = len(layout[0])
    y_max = len(layout)

def next_state(state, x, y, seat_count_func, max_seat):
    if state[y][x] == '.': return '.'
    count = seat_count_func(state, x, y)
    if state[y][x] == 'L':
        return '#' if count == 0 else 'L'
    if state[y][x] == '#':
        return '#' if count < max_seat else 'L'

def next_round(state, seat_count_func, max_seat):
    return [[next_state(state, x, y, seat_count_func, max_seat) for x in range(0, x_max)] for y in range(0, y_max)]

def get_final_round_count(seat_count_func, max_seat):
    curr = layout
    while True: 
        next = next_round(curr, seat_count_func, max_seat)
        if curr == next: return sum(c == '#' for line in next for c in line) 
        curr = next

def part1():
    seat_count_func = lambda state,x,y : sum(c == '#' for c in [state[j][i] for j in range(max(0, y - 1), min(y + 2, y_max)) for i in range(max(0, x - 1), min(x + 2, x_max)) if i != x or j != y])
    return get_final_round_count(seat_count_func, 4)

def part2():
    def seat_count_func(state,x,y):
        funcs = [lambda i: i + 1, lambda i: i - 1, lambda i: i]
        count = 0
        for f_y in funcs:
            for f_x in funcs:
                if f_x == f_y == funcs[2]: continue
                i, j = f_x(x), f_y(y)
                while 0 <= i < x_max and 0 <= j < y_max:
                    c = state[j][i]
                    if c in ['#', 'L']:
                        if c == '#':
                            count += 1
                        break
                    i, j = f_x(i), f_y(j)
        return count
    return get_final_round_count(seat_count_func, 5)
        

print(part1())
print(part2())