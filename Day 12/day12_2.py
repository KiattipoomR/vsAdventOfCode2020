shipcoor_x, shipcoor_y = 0, 0
waypointcoor_x, waypointcoor_y = 10, 1
commands = []

with open('day12.txt') as f :
    for line in f :
        line = line.strip()
        op, arg = line[0], int(line[1:])
        commands.append((op, arg))

for command, arg in commands :
    if command == 'N' :
        waypointcoor_y += arg
    elif command == 'S' :
        waypointcoor_y -= arg
    elif command == 'E' :
        waypointcoor_x += arg
    elif command == 'W' :
        waypointcoor_x -= arg
    elif command == 'F' :
        shipcoor_x += waypointcoor_x * arg
        shipcoor_y += waypointcoor_y * arg
    else :
        if command == 'L':
            arg = 360 - arg
        if arg == 90 :
            waypointcoor_x, waypointcoor_y = waypointcoor_y, -waypointcoor_x
        elif arg == 180 :
            waypointcoor_x, waypointcoor_y = -waypointcoor_x, -waypointcoor_y
        elif arg == 270 :
            waypointcoor_x, waypointcoor_y = -waypointcoor_y, waypointcoor_x

print(abs(shipcoor_x) + abs(shipcoor_y))