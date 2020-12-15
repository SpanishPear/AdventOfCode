import fileinput
from collections import Counter, defaultdict
import copy
from simplejson import dumps

inputArr = [list(i.strip()) for i in list(fileinput.input())]

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
COORDS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1, 0), (1,1)]
def clamp(value, max_val):
    return max(0, min(value, max_val))
    
def getDirectNeighbours(row, col, state,  debug=False):
    num = 0
    for y,x in COORDS:
        try: 
            if row + y < 0 or col + x < 0:
                raise IndexError
            if state[row + y][col + x] == '#':
                if debug: print(f'\t{row + y}, {col + x}')
                num += 1
        except IndexError:
            pass

    return num

def getNeighbours(row, col, state, debug=True):
    num = 0
    NUM_ROWS = len(state)
    NUM_COLS = len(state[0])
    seen = False
    for y,x in COORDS:
        x_offset = x
        y_offset = y
        while (
            0 <= row + y_offset < NUM_ROWS and 
            0 <= col + x_offset < NUM_COLS
        ): 
            if state[row + y_offset][col + x_offset] == '#':
                num += 1
                break
            elif state[row + y_offset][col + x_offset] == 'L':
                break

            x_offset += x
            y_offset += y
    
    # if row == 0 and col == 0:
    #     print(f'{num} neighbours')
    return num


def updateState(state, debug=False, partTwo=False):

    newState = copy.deepcopy(state)
    for row in range(len(state)):
        for col in range(len(state[row])): 
            neighbours = getDirectNeighbours(row, col, state) if not partTwo else getNeighbours(row,col,state)
            if debug: print(f"{row},{col} has {neighbours} neighbours")
            
            if state[row][col] != '.':
                limit = 4 if not partTwo else 5
                if neighbours >= limit:
                    newState[row][col] = 'L'
                elif neighbours == 0:
                    newState[row][col] = '#'
                else: 
                    newState[row][col] = state[row][col]
            else: 
                newState[row][col] = state[row][col]
    return newState

def partOne(debug=False) -> int:
    state = copy.deepcopy(inputArr)
    newState = updateState(state)

    
    while dumps(state) != dumps(newState):
        if debug: 
            print('-----------------------')
            print('\n'.join(str(v) for v in [''.join(i) for i in state]))
            print('--------- VS -----------')
            print('\n'.join(str(v) for v in [''.join(i) for i in newState]))

        state = newState
        newState = updateState(state)

    return (sum([item.count('#') for item in newState]))        

def partTwo(debug=True):
    state = copy.deepcopy(inputArr)
    newState = updateState(state, partTwo=True)
    print('\n'.join(str(v) for v in [''.join(i) for i in state]))
    while dumps(state) != dumps(newState):
        if debug:
            print()
            print('\n'.join(str(v) for v in [''.join(i) for i in newState]))

        state = newState
        newState = updateState(state, partTwo=True)
    
    return(sum([item.count('#') for item in newState]))     


# print(partOne())
print(partTwo())
