from collections import defaultdict

row_len, col_len = 323, 31
table = defaultdict(dict)

with open('day3.txt') as f :
    for row, line in enumerate(f) :
        for col, cell in enumerate(line) :
            table[row][col] = cell

start_row, start_col = 0, 0
answer = 0

while start_row < row_len :
    if table[start_row][start_col] == '#' :
        answer += 1

    start_row += 1
    start_col = (start_col + 3) % col_len

print(answer)