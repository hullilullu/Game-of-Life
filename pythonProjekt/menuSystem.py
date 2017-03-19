from gol import *
from readUtil import *

# Author: Christian Beck 2017

#Menu system for a game of life

#Main, calls other menus
def mainMenu(settings):
    print ("\n....MAIN MENU....\n1. RUN\n2. NEW FIELD\n3. LOAD FILE\n4. OPTIONS\n5. INSTRUCTIONS\n6. QUIT")
    s = input()
    if s == "1":
        run(settings)
    elif s ==  "2":
        changePlayField(settings)
    elif s == "3":
        loadFile(settings)
    elif s == "4":
        optionMenu(settings)
    elif s == "5":
        instruction(settings)
    elif s == "6":
        print("""
THANKS FOR PLAYING!
Made by: Christian Beck
2017

""")
    else:
        print("invalid input")
        mainMenu(settings)

# Loops over game
def run(settings):
    print("ENTER to iterate,\nq key to quit")
    input("")
    run = True
    field = settings.playField
    while run:
        drawField(field)
        for i  in range(settings.interval):
            field = iterateField(field, settings.surviveMin, settings.surviveMax,
                                 settings.spawnMin, settings.spawnMax)
        userInput = input("")
        if not userInput:
            pass
        if userInput == "q":
            run = False

    mainMenu(settings)
        
# generates new field
def changePlayField(settings):
    userInput = input("type in size of new playfield:\n")
    try:
        s = int(userInput)
        settings.playField = createField(abs(s))
        drawField(settings.playField)
    except:
        print("not an integer")
    mainMenu(settings)

#Calls readFile function and handles user interaction and error handling.
def loadFile(settings):
    userInput = input("Type in directory to load:\n")
    offsetX = int(input("offset X direction:\n"))
    offsetY = int(input("offset Y direction:\n"))
    coordList = readFile(userInput)
    if coordList: 
        for coord in coordList:
            x = coord[0]+offsetX
            y = coord[1]+offsetY
            if x > 0 and x < len(settings.playField)-1 and y > 0 and y < len(settings.playField)-1: 
                settings.playField[x][y] = True
            else:
                print("\nWARNING: A data point was outside of the grid\n")
    else:
        print("\nFailed to read file or file not found\n")
    mainMenu(settings)

#Sets global variables
def optionMenu(settings):
    s = input("....OPTIONS....\n1. Number for survival\n2. Number for spawn\n3. interval for writing out field\n4. BACK\n")
    #Sets amount of neighbours for survival
    if s == "1":
        try:
            minN = int(input("Minimum neighbours: "))
            maxN = int(input("Maximum neighbours: "))
            checkLim(minN, settings.surviveMin)
            checkLim(maxN, settings.surviveMax)
        except:
            print(" - not an integer!")
        optionMenu(settings)
    #Sets amount of neighbours that gives a new life
    elif s == "2":
        try:
            minN = int(input("Minimum neighbours: "))
            maxN = int(input("Maximum neighbours: "))
            checkLim(minN, settings.spawnMin)
            checkLim(maxN, settings.spawnMax)
        except:
            print(" - not an integer!")

        optionMenu(settings)
    #Sets amount of iterations between drawings
    elif s == "3":
        settings.interval = int(input("interval between updates: "))
        optionMenu(settings)
    elif s == "4":
        mainMenu(settings)
    else:
        print("not a valid input")
        optionMenu(settings)

#Simple function for checking if amount of neighbours given is within
#the possible values
def checkLim(n, setting):
    if n >= 0 and n < 9:
        setting = n
    else:
        print("\nERROR: Numbers must be between 0 and 8\n")

def instruction(settings):
    print("""
-------------
Game Of Life Rules.

A living cell with 2 or 3 neighbours survive.
A dead cell with 3 neighbours will start living.

(You can change these numbers in the options menu).
--------------
To choose which cells start off as living, load a file.
You can load several files on top of each ohter and offset them
so that your pattern gets repeated.

the coordinates should be given as:

x1 y1
x2 y2
x3 y3
...

-------------
To change the amount of cells, choose new field (default is a 10x10).
This will generate a new field, which you can then load your patterns in.
This also resets your cells to empty.

-------------
In the options menu you can also set frequency of which to view the field.
typ in 2 for every other, 3 for every third and so forth. (default is 1)

(PRESS ANY KEY TO RETURN TO MAIN MENU)
""")
    input()
    mainMenu(settings)

class Settings:
    def __init__(self):
        self.interval = 1
        self.surviveMin = 2
        self.surviveMax = 3
        self.spawnMin = 3
        self.spawnMax = 3
        self.playField = createField(10)

# RUN PROGRAM #
print("\n\n- Welcome to Conway's Game Of Life - \n\n")
settings = Settings() 
mainMenu(settings)
