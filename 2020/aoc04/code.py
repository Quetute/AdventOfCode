import re 

with open('input.txt', 'r') as reader:
    passports = [{match[0]: match[1] for match in re.findall(r'(\S+):(\S+)', passport)} for passport in reader.read().split("\n\n")]


def part1():
    count = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            count += 1
    return count

def part2(): 
    count = 0
    for passport in passports:
        if (checkRequiredFields(passport)
        and checkPassportLength(passport)
        and checkByr(int(passport['byr'])) 
        and checkIyr(int(passport['iyr'])) 
        and checkEyr(int(passport['eyr'])) 
        and checkHgt(passport['hgt']) 
        and checkHcl(passport['hcl']) 
        and checkEcl(passport['ecl']) 
        and checkPid(passport['pid'])):
            count += 1

    return count

def checkRequiredFields(passport):
    return len(set(passport.keys()).intersection({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})) == 7

def checkPassportLength(passport):
    return len(passport) == 7 or (len(passport) == 8 and 'cid' in passport)

def checkByr(byr):
    return 1920 <= byr and byr <= 2002

def checkIyr(iyr):
    return 2010 <= iyr and iyr <= 2020

def checkEyr(eyr):
    return 2020 <= eyr and eyr <= 2030

def checkHgt(hgt):
    hgtm = re.match(r'^(\d+)(cm|in)$', hgt)
    if hgtm is None:
        return False
    heightValue = int(hgtm.group(1))
    heightUnit = hgtm.group(2)
    return (heightUnit == 'cm' and 150 <= heightValue and heightValue <= 193) or (heightUnit == 'in' and 59 <= heightValue and heightValue <= 76)

def checkHcl(hcl): 
    return re.match(r'^#[0-9a-f]{6}$', hcl) is not None

def checkEcl(ecl): 
    return re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', ecl) is not None

def checkPid(pid): 
    return re.match(r'^\d{9}$', pid) is not None

print(part1())
print(part2())
