coor_x, coor_y = 0, 0
direction = 90
commands = []

with open('day12.txt') as f :
    for line in f :
        line = line.strip()
        op, arg = line[0], int(line[1:])
        commands.append((op, arg))

for command, arg in commands :
    if command == 'N' :
        coor_y += arg
    elif command == 'S' :
        coor_y -= arg
    elif command == 'E' :
        coor_x += arg
    elif command == 'W' :
        coor_x -= arg
    elif command == 'L' :
        direction = (direction - arg) % 360
    elif command == 'R' :
        direction = (direction + arg) % 360
    elif command == 'F' :
        if direction == 0 :
            coor_y += arg
        if direction == 90 :
            coor_x += arg
        if direction == 180 :
            coor_y -= arg
        if direction == 270 :
            coor_x -= arg
    print(coor_x, coor_y, direction)

print(abs(coor_x) + abs(coor_y))