with open('input.txt', 'r') as reader:
    draws = list(map(lambda v: int(v), reader.readline().split(",")))
    lines = [line for line in reader.read().splitlines()]
    boards = []
    for i, line in enumerate(lines):
        if i % 6 == 0:
            boards.append([])
        else:
            boards[-1].append([int(v) for v in line.split()])


def part1():
   for i in range(1, len(draws)):
       current_draws = draws[0:i]
       for board in boards:
           if has_board_won(board, current_draws):
               return get_score(board, current_draws)

def part2():
    boards_count = len(boards)
    winning_boards_idx = []
    for i in range(1, len(draws)):
        current_draws = draws[0:i]
        for i, board in enumerate(boards):
            if i not in winning_boards_idx and has_board_won(board, current_draws):
                winning_boards_idx.append(i)
                if len(winning_boards_idx) == boards_count:
                    return get_score(board, current_draws)

def has_board_won(board, winning_draws):
    # Better perfs could be obtained with preprocessing boards into rows and columns and clever indexing by values
    for line in board:
        if all(map(lambda v: v in winning_draws, line)):
            return True
    
    for column in [*zip(*board)]:
        if all(map(lambda v: v in winning_draws, column)):
            return True
    
    return False

def get_score(board, winning_draws):
    return winning_draws[-1] * sum([v if v not in winning_draws else 0 for line in board for v in line])

print(part1())
print(part2())
