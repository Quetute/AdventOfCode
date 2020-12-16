import sys 

with open('input.txt', 'r') as reader:
    earliest = int(reader.readline())
    ids = [i for i in reader.readline().strip().split(',')]

def part1():
    # depart = min((id * (earliest // id) + 1) for id in ids)
    min = sys.maxsize * 2
    for id in ids:
        if id == 'x':
            continue
        id = int(id)
        tmp = id * ((earliest // id) + 1)
        if tmp < min:
            min = tmp
            bus = id

    return (min - earliest) * bus

def part2():
    x = []
    for idx, id in enumerate(ids):
        if id != 'x':
            x.append((int(id), idx))

    x = sorted(x, key=lambda i: i[0], reverse=True)
    p = 1
    t = 0
    for i in x:
        while (t + i[1]) % i[0] != 0:
            t += p
        p *= i[0]
    return t
        
            
print(part1())
print(part2())