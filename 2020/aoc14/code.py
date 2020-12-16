import re 

with open('input.txt', 'r') as reader:
    lines = [re.match(r'(\S+)\s*=\s*(\S+)', line).groups() for line in reader.readlines()]

def compute(apply_mask):
    mem = {}
    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            idx = int(re.match(r'mem\[(\d+)\]', line[0]).groups()[0])
            apply_mask(mem, idx, line[1], mask)
    return sum(mem[k] for k in mem)

def to_int(bin_array):
    return int(''.join(bin_array), 2)

def part1():
    def apply_mask(mem, idx, val, mask):
            val = f'{int(val):036b}'
            mem[idx] = to_int([val[i] if mask[i] == 'X' else mask[i] for i in range(0, len(val))])
    return compute(apply_mask)

def part2():
    def apply_bit(adresses, bit):
        return list(map(lambda a: bit + a ,adresses))

    def get_all_adresses(adress):
        if len(adress) == 0:
            return ['']
        if adress[0] == 'X':
            ads = get_all_adresses(adress[1:])
            return apply_bit(ads, '0') + apply_bit(ads, '1')
        if adress[0] != 'X':
            return apply_bit(get_all_adresses(adress[1:]), adress[0])
        
    def apply_mask(mem, idx, val, mask):
        idx = f'{int(idx):036b}'
        idx = ''.join([str(int(idx[i]) | int(mask[i])) if mask[i] != 'X' else mask[i] for i in range(0, len(idx))])
        # print(idx)

        for adress in get_all_adresses(idx):
            mem[to_int(adress)] = int(val)

    return compute(apply_mask)

print(part1())
print(part2())