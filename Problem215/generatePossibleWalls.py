# Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal × vertical dimensions) such that, for extra strength, the gaps between horizontally-adjacent
# bricks never line up in consecutive layers, i.e. never form a "running crack".
# There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.
# Calculate W(32,10).

import os
import sys
import itertools

lengthOfRows = 32 #length of rows to be used in creating wall - rows file MUST be generated beforehand using generatePossibleRows.py

with open('Problem215/' + str(lengthOfRows) + 'rows.txt') as file: #import rows from file as array
    rows = file.readlines()
file.close()
rows = [i.strip() for i in rows] #rows is list of rows

def generatePossibleWalls(rows, height):
    walls = open(os.path.join(sys.path[0], "%dx%dwall.txt" %(lengthOfRows, height)), "a") #create file containing all possible rows given list of rows and height of wall
    for r in itertools.product(rows, repeat=height):
        for i in range(height):
            walls.write(r[i] + '\n')
        walls.write('\n')
    walls.close()

generatePossibleWalls(rows, 10)