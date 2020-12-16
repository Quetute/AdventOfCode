import math

with open('input.txt', 'r') as reader:
    instructions = [(instruction[0], int(instruction[1:])) for instruction in reader.readlines()]

def north(pos, v):
    pos['x'] += v

def south(pos, v):
    pos['x'] -= v

def west(pos, v):
    pos['y'] -= v

def east(pos, v):
    pos['y'] += v

def forward(pos, v):
    ACTIONS[pos['o']](pos, v)

DIRS = ['N', 'E', 'S', 'W']

def left(pos, v):
    v = v // 90
    pos['o'] = DIRS[(DIRS.index(pos['o']) - v) % len(DIRS)]

def right(pos, v):
    v = v // 90
    pos['o'] = DIRS[(DIRS.index(pos['o']) + v) % len(DIRS)]

ACTIONS = {
    'N': north,
    'E': east,
    'S': south,
    'W': west,
    'F': forward,
    'L': left,
    'R': right
}

def north2(pos, v):
    pos['wp']['y'] += v

def south2(pos, v):
    pos['wp']['y'] -= v

def west2(pos, v):
    pos['wp']['x'] -= v

def east2(pos, v):
    pos['wp']['x'] += v

def forward2(pos, v):
    pos['x'] += pos['wp']['x'] * v 
    pos['y'] += pos['wp']['y'] * v 

def left2(pos, v):
    x = pos['wp']['x']
    y = pos['wp']['y']
    pos['wp']['x'] = int(math.cos(math.radians(v/math.pi)*math.pi)) * x - int(math.sin(math.radians(v/math.pi)*math.pi)) * y
    pos['wp']['y'] = int(math.cos(math.radians(v/math.pi)*math.pi)) * y + int(math.sin(math.radians(v/math.pi)*math.pi)) * x

def right2(pos, v):
    x = pos['wp']['x']
    y = pos['wp']['y']
    pos['wp']['x'] = int(math.cos(math.radians(v/math.pi)*math.pi)) * x + int(math.sin(math.radians(v/math.pi)*math.pi)) * y
    pos['wp']['y'] = int(math.cos(math.radians(v/math.pi)*math.pi)) * y - int(math.sin(math.radians(v/math.pi)*math.pi)) * x

ACTIONS2 = {
    'N': north2,
    'E': east2,
    'S': south2,
    'W': west2,
    'F': forward2,
    'L': left2,
    'R': right2
}

def part1(): 
    pos = {'x':0, 'y':0, 'o': 'E'}
    for instruction in instructions:
        ACTIONS[instruction[0]](pos, instruction[1])

    return abs(pos['x']) + abs(pos['y'])

def part2():
    pos = {'x':0, 'y':0, 'wp': {'x': 10, 'y': 1}}
    for instruction in instructions:
        ACTIONS2[instruction[0]](pos, instruction[1])
        print(pos)

    return abs(pos['x']) + abs(pos['y'])

print(part1())
print(part2())