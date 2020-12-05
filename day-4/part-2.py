import re

input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(str(line))

formatted = []

i = 0
flag = True

for line in input:
    if line == '':
        i += 1
        flag = True
    else:
        if flag:
            formatted.append([])
            flag = False

        for item in line.split(' '):
            formatted[i].append(item)


def check_byr(item: str) -> bool:
    if re.match(r'^\d{4}$', str(item[4:])) == None:
        return False

    return 1920 <= int(item[4:]) <= 2002


def check_iyr(item: str) -> bool:
    if re.match(r'^\d{4}$', str(item[4:])) == None:
        return False

    return 2010 <= int(item[4:]) <= 2020


def check_eyr(item: str) -> bool:
    if re.match(r'^\d{4}$', str(item[4:])) == None:
        return False

    return 2020 <= int(item[4:]) <= 2030


def check_hgt(item: str) -> bool:
    if str(item[-2:]) == 'in':
        return 59 <= int(item[4:-2]) <= 76

    if str(item[-2:]) == 'cm':
        return 150 <= int(item[4:-2]) <= 193

    return False


def check_hcl(item: str) -> bool:
    return re.match(r'^#[0-9a-f]{6}$', str(item[4:])) != None


ecs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_ecl(item: str) -> bool:
    return item[4:] in ecs


def check_pid(item: str) -> bool:
    return re.match(r'^\d{9}$', str(item[4:])) != None
    # return True


valid_pp = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
semi_valid_pp = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
valids = 0
semis = 0

for passport in formatted:
    checks = []

    if not len(passport) < 7:
        for item in passport:
            id = item[:3]
            if id == 'byr':
                if check_byr(item):
                    checks.append(id)
            elif id == 'iyr':
                if check_iyr(item):
                    checks.append(id)
            elif id == 'eyr':
                if check_eyr(item):
                    checks.append(id)
            elif id == 'hgt':
                if check_hgt(item):
                    checks.append(id)
            elif id == 'hcl':
                if check_hcl(item):
                    checks.append(id)
            elif id == 'ecl':
                if check_ecl(item):
                    checks.append(id)
            elif id == 'pid':
                if check_pid(item):
                    checks.append(id)

        s_checks = sorted(checks)

        if s_checks == valid_pp:
            valids += 1
        elif s_checks == semi_valid_pp:
            semis += 1

print(f'Valids: {valids}')
print(f'Semis: {semis}')
print(f'Total: {valids + semis}')
