import fileinput
from functools import reduce
ROW_MAX = 127
COL_MAX = 7

inputArr = [list(line.strip()) for line in fileinput.input()]

def partOne():
    seatIDs = set()
    for item in inputArr:
        row = item[:7]
        col = item[7:]
        

        # find the row
        lower = 0
        upper = ROW_MAX
        for half in row:
            midpoint = ( lower + upper ) // 2 
            if half == "B":
                lower = midpoint + 1
            if half == "F":
                upper = midpoint 
        
        correct_row = midpoint if half == "F" else midpoint + 1

        # find the col
        lower = 0
        upper = COL_MAX            
        for half in col:
            midpoint = ( lower + upper ) // 2
            if half == "R":
                lower = midpoint + 1
            if half == "L":
                upper = midpoint
        
        correct_col = midpoint if half == "L" else midpoint + 1

        # add to set
        seatIDs.add(correct_col + correct_row*8)

        # print(f'row: {correct_row} col: {correct_col}, seatID={correct_row*8 + correct_col}')

    #find max in set
    print(max(seatIDs))


def partTwo():
    seats = set()
    for item in inputArr:
        row = item[:7]
        col = item[7:]
        

        # find the row
        lower = 0
        upper = ROW_MAX
        for half in row:
            midpoint = ( lower + upper ) // 2 
            if half == "B":
                lower = midpoint + 1
            if half == "F":
                upper = midpoint 
        
        correct_row = midpoint if half == "F" else midpoint + 1

        # find the col
        lower = 0
        upper = COL_MAX            
        for half in col:
            midpoint = ( lower + upper ) // 2
            if half == "R":
                lower = midpoint + 1
            if half == "L":
                upper = midpoint
        
        correct_col = midpoint if half == "L" else midpoint + 1

        # add to set
        seats.add((correct_row, correct_col))


    all_seats = sorted(set([(x,y) for x in range(11,117) for y in range(0,8)]), key=lambda x:(x[0], x[1]))
    sorted_seats = sorted(seats, key=lambda x:(x[0], x[1]))
    print(set(all_seats).difference(sorted_seats))
    
    # print(sorted_seats)

partOne()
partTwo()