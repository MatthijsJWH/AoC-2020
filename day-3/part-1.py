input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(str(line))

down = 1
right = 3
i = down
j = 0
path = ''

while i < len(input):
    j += right

    line = input[i]
    place = j % len(line)

    path += line[place]
    i += down

trees = path.count('#')

print(trees)
