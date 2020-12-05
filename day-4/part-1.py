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

print(formatted)

valid_pp = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
semi_valid_pp = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
valids = 0
semis = 0

for passport in formatted:
    checks = []

    if not len(passport) < 7:
        for item in passport:
            checks.append(item[:3])

        s_checks = sorted(checks)

        if s_checks == valid_pp:
            valids += 1
        elif s_checks == semi_valid_pp:
            semis += 1

print(f'Valids: {valids}')
print(f'Semis: {semis}')
print(f'Total: {valids + semis}')
