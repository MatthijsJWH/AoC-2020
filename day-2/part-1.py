input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(str(line))

valids = 0

for pw in input:
    dash = pw.find('-')
    space = pw.find(' ')
    colon = pw.find(':')

    min = int(pw[:dash])
    max = int(pw[dash+1:space])
    char = pw[colon-1]

    word = pw[colon+1:]
    count = word.count(char)
    if min <= count <= max:
        valids += 1

print(f'valid pws: {valids}')