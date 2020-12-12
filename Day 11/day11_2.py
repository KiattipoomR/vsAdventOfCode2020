from copy import deepcopy

seat_grid = {}

def total_occupied_seats(grid) :
    occupied_seats = 0
    for row in sorted(grid.keys()) :
        for col in sorted(grid[row].keys()) :
            if grid[row][col] == '#' :
                occupied_seats += 1
    return occupied_seats

def find_adjacent_occupied(row, col) :
    occupied_seats = 0
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    for direction in directions :
        row_copy, col_copy = row, col
        while True :
            row_copy += direction[0]
            col_copy += direction[1]
            try :
                seat_in_sight = seat_grid[row_copy][col_copy]
                if seat_in_sight != '.' :
                    if seat_in_sight == '#' : occupied_seats += 1
                    break
            except KeyError :
                break
    return occupied_seats

with open('day11.txt') as f :
    for row, line in enumerate(f) :
        line = line.strip()
        seat_grid[row] = {}
        for col, seat in enumerate(line) :
            seat_grid[row][col] = seat

iteration = 0

while True :
    changed_seats = 0
    seat_grid_copy = deepcopy(seat_grid)
    for row in sorted(seat_grid.keys()) :
        for col in sorted(seat_grid[row].keys()) :
            if seat_grid[row][col] == 'L' and find_adjacent_occupied(row, col) == 0 :
                seat_grid_copy[row][col] = '#'
                changed_seats += 1
            elif seat_grid[row][col] == '#' and find_adjacent_occupied(row, col) > 4 :
                seat_grid_copy[row][col] = 'L'
                changed_seats += 1
    seat_grid = seat_grid_copy
    if changed_seats == 0 : break
    iteration += 1

print(total_occupied_seats(seat_grid))