import fileinput
from collections import Counter, defaultdict
import math

inputArr = [line.strip() for line in fileinput.input()]

def partOne() -> int: 
    directions = {
        0 : 'N',
        90: 'E',
        180: 'S',
        270: 'W'
    }
    # move NSEW
    # turn LR
    # move F
    direction = 90 # east, degrees
    east = 0
    north = 0
    for item in inputArr:
        cmd = item[0]
        val = int(item[1:])
        print(cmd, val)
        if cmd == 'N':
            north += val
        
        elif cmd == 'S':
            north -= val
        
        elif cmd == 'E':
            east += val
        
        elif cmd == 'W':
            east -= val
        
        elif cmd == 'L':
            direction -= val
            direction %= 360

        elif cmd == 'R': 
            direction += val
            direction %= 360
        
        elif cmd == 'F':
            dir = directions[direction]
            if dir == 'N':
                north += val
            elif dir == 'S':
                north -= val
            elif dir == 'E':
                east += val
            elif dir == 'W':
                east -= val
    print(abs(north)+ abs(east))


def partTwo():
    moves = {"N": (1, 0), "S": (-1, 0), "E": (0, -1), "W": (0, 1)}
    direction_id = 0  # EAST
    x, y = 0, 0
    waypoint_x, waypoint_y = 1, -10 # 1 NORTH, 10 EAST  (relative coords)
    for inst in inputArr:
        action = inst[0]
        number = int(inst[1:])
        if action == "F":
            x, y = x + waypoint_x*number, y + waypoint_y*number
        elif action in moves:
            dx, dy = moves[action]
            waypoint_x, waypoint_y = waypoint_x + (dx * number), waypoint_y + (dy * number)
        else:  # action is a turn
            if number == 180:
                waypoint_x = -waypoint_x
                waypoint_y = -waypoint_y
            elif (action == "R" and number == 90) or (action == "L" and number == 270):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            elif (action == "R" and number == 270) or (action == "L" and number == 90):
                waypoint_x, waypoint_y = - waypoint_y, waypoint_x
    
    print(abs(x) + abs(y))

# partOne()
partTwo()