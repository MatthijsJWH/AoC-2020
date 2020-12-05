input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        input.append(str(line))

all_passes = []

for boarding_pass in input:
    l_row = 0
    h_row = 128
    l_col = 0
    h_col = 8

    for char in boarding_pass:
        if char == 'F':
            h_row = (h_row - l_row) / 2 + l_row

        elif char == 'B':
            l_row = (h_row - l_row) / 2 + l_row

        elif char == 'L':
            h_col = (h_col - l_col) / 2 + l_col

        elif char == 'R':
            l_col = (h_col - l_col) / 2 + l_col

    if not (l_row == h_row - 1 and l_col == h_col - 1):
        print('An error has been made: ')
        print(boarding_pass)

    else:
        id = int(l_row * 8 + l_col)
        all_passes.append(id)

sorted_passes = sorted(all_passes)
my_pass = 0

for i in range(0, sorted_passes[-1]):
    if i not in sorted_passes:
        if (i - 1) in sorted_passes and (i + 1) in sorted_passes:
            my_pass = i

print(my_pass)
