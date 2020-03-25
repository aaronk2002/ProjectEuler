def getCracks(row):
    rowList = [int(brick) for brick in row]
    cracks = [] #list of all cracks in row
    index = 1
    while index < len(rowList):
        sum = 0
        for brick in range(index):
            sum += rowList[index]
        cracks.append(sum)
        index += 1
    return(cracks)

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
    
    goodWalls = 0
    for wall in walls:
        for row in wall:
            print(getCracks(row))


checkWalls('12x2wall.txt')