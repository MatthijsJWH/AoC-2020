input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(int(line))

i = 0
for number in input:
    i += 1
    j = i
    x = number

    while (j < len(input)):
        y = input[j]

        if (x + y) == 2020:
            print(x*y)

        j += 1