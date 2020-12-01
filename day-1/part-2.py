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
        k = j + 1
        y = input[j]

        while (k < len(input)):
            z = input[k]

            if (x + y + z) == 2020:
                print(x * y * z)

            k += 1

        j += 1