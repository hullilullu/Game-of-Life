# Author: Christian Beck 2017

#game logic for a  Conway's game of life

# gives a set of lists within lists that the game takes place in
def createField(size):
    playingField = []
    for i in range(size+2):
        column = []
        for i in range(size+2):
            column.append(False)
        playingField.append(column)
    return playingField

#Iterates the field holding the boolean values
def iterateField(playingField, surviveMin = 2,
                 surviveMax = 3, spawnMin = 3, spawnMax = 3):
    size = len(playingField)-2
    newField = createField(size)
    #Iterates over all cells
    for i1 in range (1,size+1):
        for i2 in range (1,size+1):
            neighbour = 0
            #iterates over all neighbours for each cell (including the cell)
            for i3 in range(-1, 2):
                for i4 in range(-1, 2):
                    #If checked cell is true increase neighbour count
                    if playingField[(i1+i3-1)%size+1][(i2+i4-1)%size+1] == True:
                        neighbour += 1
            #if living cell
            if playingField[i1][i2] == True:
                neighbour -= 1
                if neighbour >= surviveMin and neighbour <= surviveMax:
                    newField[i1][i2] = True
            # else if dead cell
            elif playingField[i1][i2] == False:
                    if neighbour >= spawnMin and neighbour <= spawnMax:
                        newField[i1][i2] = True

    return newField

#Presents the field to the user.           
def drawField(playingField):
    size = len(playingField)-2
    for i1 in range (1,size+1):
        for i2 in range (1,size+1):
            if playingField[i1][i2] == True:
                print("%2s" % ("#"), end="")
            else:
                print("%2s" %("_"),end="")
        print("\n")



## SIMPLE TEST

##testF = createField(6)
##testF[1][2] = True
##testF[2][3] = True
##testF[3][3] = True
##testF[3][2] = True
##testF[3][1] = True
##
##for i in range(20):
##    drawField(testF)
##    testF = iterateField(testF)
##    print("")
