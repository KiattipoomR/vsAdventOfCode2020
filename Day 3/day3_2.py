from collections import defaultdict
import math

row_len, col_len = 323, 31
table = defaultdict(dict)

with open('day3.txt') as f :
    for row, line in enumerate(f) :
        for col, cell in enumerate(line) :
            table[row][col] = cell

amount_entries = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
answer = 1

def travel(row_amount, col_amount) :
    start_row, start_col = 0, 0
    answer = 0

    while start_row < row_len :
        if table[start_row][start_col] == '#' :
            answer += 1

        start_row += row_amount
        start_col = (start_col + col_amount) % col_len

    return answer

for row_entry, col_entry in amount_entries :
    entry_answer = travel(row_entry, col_entry)
    print(entry_answer)
    answer *= entry_answer

print(answer)