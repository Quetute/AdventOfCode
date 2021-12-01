from functools import lru_cache

with open('input.txt', 'r') as reader:
    layout = [[c for c in line.strip()] for line in reader.readlines()]

def count_func(state, x, y, z):
        # print("+++++++")
        # print(f"state[{z}][{y}][{x}]={state[z][y][x]}")
        count = 0
        for k in range(max(0, z - 1), min(z + 2, len(state))):
            for j in range(max(0, y - 1), min(y + 2, len(state[k]))):
                for i in range(max(0, x - 1), min(x + 2, len(state[k][j]))):
                    if state[k][j][i] == '#' and (i != x or j != y or k != z):
                        count += 1
        # print(f"count={count}")
        # input()
        return count

def next_state(state, x, y, z):
    count = count_func(state, x, y, z)
    if state[z][y][x] == '#': return '#' if 2 <= count <= 3 else '.'
    if state[z][y][x] == '.': return '#' if count == 3 else '.'

def expand_state(state):
    ret = []
    z_max = len(state)
    y_max = len(state[0])
    x_max = len(state[0][0])
    for k in range(z_max + 2):
        k_range = []
        ret.append(k_range)
        for j in range(y_max + 2):
            j_range = []
            k_range.append(j_range)
            for i in range(x_max + 2):
                if 0  in {i,j,k} or k == z_max +1 or j == y_max + 1 or i == x_max + 1:
                    j_range.append('.')
                else:
                    j_range.append(state[k - 1][j - 1][i - 1])
    return ret

def expand_state2(state):
    if isinstance(state, list):
        return get_filling(state[0]) + [expand_state2(e) for e in state] + get_filling(state[0])
    else:
        return ['.', state, '.']


def get_filling(state):
    if isinstance(state, list):
        return [get_filling(state[0]) * 3]
    else:
        return ['.']

def next_round(state):
    state = expand_state(state)
    state2 = expand_state2(state)
    print('\n\n'.join(['\n'.join([''.join(y) for y in z]) for z in state]))
    print('\n\n'.join(['\n'.join([''.join(y) for y in z]) for z in state2]))
    print(state == state2)
    input()
    return [[[next_state(state, x, y ,z) for x in range(len(state[z][y]))] for y in range(len(state[z]))] for z in range(len(state))]

def get_final_round_count(max_turn, dim):
    curr = layout
    for i in range(dim - 2):
        curr = [curr]

    for turn in range(max_turn):
        # print("==========")
        # print('\n\n'.join(['\n'.join([''.join(y) for y in z]) for z in curr]))
        curr = next_round(curr)

    return count_all(curr)

def count_all(state):
    if isinstance(state, list):
        return sum(count_all(e) for e in state)
    else:
        return 1 if state == '#' else 0

def part1():
    return get_final_round_count(6,3)

def part2():
    return get_final_round_count(6,4)

print(part1())
