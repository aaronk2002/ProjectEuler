def checkWalls(wallsFile):
    with open('Problem215/' + wallsFile) as file: #import rows from file as array
        unseparatedWalls = file.readlines()
    file.close()
    unseparatedWalls = [i.strip() for i in unseparatedWalls]

    walls = [] #create list of lists representing walls
    wallCount = 0
    wall = []
    while(wallCount < len(unseparatedWalls)):
        if(unseparatedWalls[wallCount] != ''):
            wall.append(unseparatedWalls[wallCount])
        else:
            walls.append(wall)
            wall = []
        wallCount += 1

checkWalls('12x2wall.txt')