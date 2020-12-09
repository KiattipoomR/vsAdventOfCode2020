entries = []
seat_ids = set()

with open('day5.txt') as f :
    for line in f :
        entries.append(line)

for entry in entries :
    row_range = [0, 127]
    col_range = [0, 7]

    for letter in entry :
        row_half = (row_range[1] - row_range[0] + 1) // 2
        col_half = (col_range[1] - col_range[0] + 1) // 2

        if letter == 'F' :
            row_range[1] -= row_half
        elif letter == 'B' :
            row_range[0] += row_half
        elif letter == 'L' :
            col_range[1] -= col_half
        elif letter == 'R' :
            col_range[0] += col_half

    seat_id = (row_range[0] * 8) + col_range[0]

    seat_ids.add(seat_id)

all_set_ids = set(range(min(seat_ids), max(seat_ids) + 1))

print(all_set_ids.difference(seat_ids))