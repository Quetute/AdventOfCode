with open('input.txt', 'r') as reader:
    lines = [[int(v) for v in line] for line in reader.read().splitlines()]

def is_low_point(i, j):
    return not ((i > 0 and lines[i][j] >= lines[i - 1][j]) or 
       (i < len(lines) - 1 and lines[i][j] >= lines[i + 1][j]) or
       (j > 0 and lines[i][j] >= lines[i][j - 1]) or
       (j < len(lines[i]) - 1 and lines[i][j] >= lines[i][j + 1]))

def part1():
    return sum([lines[i][j] + 1 for i in range(len(lines)) for j in range(len(lines[i])) if is_low_point(i , j)])

def get_basin(i, j, basin):
    if (i,j) in basin or lines[i][j] == 9:
        return

    basin.add((i,j))
    if i > 0 and lines[i][j] < lines[i - 1][j]:
        get_basin(i - 1, j, basin)

    if i < len(lines) - 1 and lines[i][j] < lines[i + 1][j]:
        get_basin(i + 1, j, basin)
    
    if j > 0 and lines[i][j] < lines[i][j - 1]:
        get_basin(i, j - 1, basin)

    if j < len(lines[i]) - 1 and lines[i][j] < lines[i][j + 1]:
        get_basin(i, j + 1, basin)

def part2():
    basins = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if is_low_point(i, j):
                basin = set()
                get_basin(i, j, basin)
                basins.append(len(basin))

    basins.sort()
    print(basins)
    return basins[-1] * basins[-2] * basins[-3]

print(part1())
print(part2())
