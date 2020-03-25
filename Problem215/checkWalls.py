def getCracks(row):
    rowList = [int(brick) for brick in row]
    cracks = [] #list of all cracks in row
    index = 1
    while index < len(rowList):
        sum = 0
        for brick in range(index):
            sum += rowList[brick]
        cracks.append(sum)
        index += 1
    return(cracks)

def commonMember(a, b):
    if(set(a) & set(b)):
        return(True)
    else:
        return(False)

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
        crackSet = []
        for row in wall:
            crackSet.append(getCracks(row))
        #print(crackSet)
        for i in range(len(crackSet) - 1):
            #print(crackSet[i])
            #print(crackSet[i+1])
            if(commonMember(crackSet[i], crackSet[i+1])):
                #print('Continuing')
                break
            if(i+1 == len(crackSet) - 1):
                #print('Adding wall')
                goodWalls += 1
        else:
            continue
    print(goodWalls)

checkWalls('9x3wall.txt')