# Author: Christian Beck 2017

#reads files with x and y coordinates into lists [x, y] within a list
#
# FILE FORMAT:
# x1 y1
# x2 y2
# ...
def readFile(directory):
    returnList = []
    try:
        f = open(directory, "r")
        lines = f.readlines()
        for line in lines:
            rawCoord = line.split(" ")
            coord = (int(rawCoord[0]),int(rawCoord[1]))
            returnList.append(coord)
    except:
        return None
    return returnList
