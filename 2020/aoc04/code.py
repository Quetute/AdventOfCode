import re 

with open('input.txt', 'r') as reader:
    passports = [{match[0]: match[1] for match in re.findall(r'(\S+):(\S+)', passport)} for passport in reader.read().split("\n\n")]

def check_height(hgt):
    m = re.match(r'^(\d+)(cm|in)$', hgt)
    return m and {
        'cm': lambda height: 150 <= int(height) <= 193,
        'in': lambda height: 59 <= int(height) <= 76
    }[m.group(2)](m.group(1))
 
FIELD_CHECKS = {
    'byr' : lambda byr: 1920 <= int(byr) <= 2002,
    'iyr' : lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr' : lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt' : check_height,
    'hcl' : lambda hcl: re.match(r'^#[0-9a-f]{6}$', hcl) is not None,
    'ecl' : lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid' : lambda pid: re.match(r'^\d{9}$', pid) is not None
}

def check_required_fields(passport):
    return set(FIELD_CHECKS) - set(passport) | {'cid'} == {'cid'}

def part1():
    return sum(check_required_fields(passport) for passport in passports)

def part2():
    return sum(check_required_fields(passport) and all(FIELD_CHECKS[field](passport[field]) for field in FIELD_CHECKS) for passport in passports)

print(part1())
print(part2())