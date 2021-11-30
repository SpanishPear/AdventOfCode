import fileinput
from functools import reduce

inputArr = [list(line.strip()) for line in fileinput.input()]
WIDTH = len(inputArr[0])
HEIGHT = len(inputArr)

def partOne(right, down):
    # right, down = slope
    xcoord = 0
    ycoord = 0
    numTrees = 0
    
    while (ycoord < HEIGHT ):
        if (inputArr[ycoord][xcoord] == '#'):
            numTrees += 1

        ycoord =  ycoord + down 
        xcoord = (xcoord + right) % WIDTH


    return numTrees

def partTwo():
    return  reduce((lambda x,y: x * y), [partOne(right, down) for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]])


print(partOne(3, 1))
print(partTwo())