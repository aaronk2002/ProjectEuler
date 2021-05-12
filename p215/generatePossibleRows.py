# Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal × vertical dimensions) such that, for extra strength, the gaps between horizontally-adjacent
# bricks never line up in consecutive layers, i.e. never form a "running crack".
# There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.
# Calculate W(32,10).

import os
import sys

def generatePossibleRows(row, width): #generates all possible rows using bricks of length 2 and 3 given initial row (for recursion) and width of row
    rows = open(os.path.join(sys.path[0], "%srows.txt" %width), "a")
    length = 0 #determine length of initial row
    for i in row:
        length += i
    if not length < width - 4: #edge cases
        if length == width - 4:
            row.append(2)
            row.append(2)
        elif length == width - 3:
            row.append(3)
        elif length == width - 2:
            row.append(2)
        strRow = ''
        for brick in row:
            strRow += str(brick)
        rows.write(strRow + '\n')
    else: #if not an edge case, recursively generate row
        row1 = row.copy()
        row2 = row.copy()
        row1.append(2)
        row2.append(3)
        generatePossibleRows(row1, width)
        generatePossibleRows(row2, width)
    rows.close()

generatePossibleRows([], 32)