def calculate_next_direction(dx,dy):
    if dx == 0 and dy == 1:
        return 'N'
    elif dx == -1 and dy == 0:
        return 'W'
    elif dx == 0 and dy == -1:
        return 'S'
    else:
        return 'E'

def robotSim(direction, position, commands):
    direction_map = {'N':(0,1), 'W':(-1,0),'S':(0,-1),'E':(1,0)}
    dx, dy = direction_map[direction]
    x, y = position
    for command in commands:
        if command == 'L':
            dx, dy = -dy, dx
            current_direction = calculate_next_direction(dx,dy)
        elif command == 'R':
            dx, dy = dy, -dx
            current_direction = calculate_next_direction(dx,dy)
        else:
            x, y =  + dx, y + dy
    return (current_direction, x, y)
print(robotSim('N', (7,3), 'LAARA'))
