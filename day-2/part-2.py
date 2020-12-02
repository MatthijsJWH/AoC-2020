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

    pos_1 = int(pw[:dash])
    pos_2 = int(pw[dash+1:space])
    char = pw[colon-1]
    word = pw[colon+1:]

    if (word[pos_1] == char) ^ (word[pos_2] == char):
        valids += 1

print(f'valid pws: {valids}')