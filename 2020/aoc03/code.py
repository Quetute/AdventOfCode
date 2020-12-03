
with open('input.txt', 'r') as reader:
    lines = reader.readlines()
    map = []
    for line in lines: 
        map.append(list(line.strip()))
        
def checkSlope(xSlope, ySlope): 
    x = 0
    y = 0
    yend = len(map)
    xend = len(map[0])
    count = 0
    while y < yend:
        if map[y][x] == '#':
            count += 1
        x = (x + xSlope) % xend
        y += ySlope
    return count

def part1():
    return checkSlope(3,1)

def part2():
    return checkSlope(1,1) * checkSlope(3,1) * checkSlope(5,1) * checkSlope(7,1) * checkSlope(1,2)

print(part1())
print(part2())
