input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(str(line))

def count_trees(down: int, right: int) -> int:
    i = down
    j = 0
    path = ''

    while i < len(input):
        j += right

        line = input[i]
        place = j % len(line)

        path += line[place]
        i += down

    return path.count('#')

result = count_trees(1, 1) * count_trees(1, 3) * count_trees(1, 5) * count_trees(1, 7) * count_trees(2, 1)
print(result)
