#Created by Eli Slothower (Andrew ID: eslothow)

######################################################################
#Imports
######################################################################

from cmu_112_graphics import *
from Animal import *
from Sheep import *
from Wolf import *
import random

######################################################################
#Animal Code
######################################################################

animalCount = {'Wolf': 10, 'Sheep': 10}
SheepNames = set()
WolfNames = set()
SheepPosition = []
WolfPosition = []

def initializeAnimals(app):

    for key in animalCount:
        for _ in range(animalCount[key]):
            
            while True:
                number = random.randrange(1000000000000)
                animalName = '%s%s' % ([key], number)
                if animalName not in globals()[key+'Names']: 
                    globals()[key+'Names'].add(animalName)
                    globals()[animalName] = eval(key+'()') 
                    globals()[key+'Position'].append([random.randrange((app.margin + 10), (app.width/2 + 5)), random.randrange(app.margin + 12, app.height-app.margin-12)])

                    # print(f'This is {key.lower()} {animalName}')
                    print(f'This is the sheep position list now: {SheepPosition}')
                    # print(f'This is the wolf position list now: {WolfPosition}')
                    break



######################################################################
#App Started
######################################################################

def appStarted(app):

    #System Settings
    ###############################################

    #app.mode = "titleScreen"
    app.mode = 'simulateScreen'
    app._root.resizable(False, False) #Contributed by Anita (TA)
    app.timerDelay = 0

    #Code for terrain generation
    ###############################################
    app.rows = 30
    app.cols = 30
    app.cellSize = 25
    app.margin = 25
    app.gridWidth  = app.width//2 #this makes the grid go to the left side of the screen
    app.gridHeight = app.height - 2*app.margin
    app.colors = ['green', 'tan', 'blue']
    app.waterPuddles = random.randrange(3)
    app.waterAmount = 'Regular'
    app.flowerColorOptions = ['pink', 'red', 'purple', 'yellow', 'orange']
    app.cellColorsList = getCellColorsList(app, app.rows, app.cols)

    #Code for animals
    ###############################################
    initializeAnimals(app)
    app.wolfImage = app.scaleImage(app.loadImage('assets/Modified/black_wolf.png'), 1/10)
    app.sheepImage = app.scaleImage(app.loadImage('assets/Modified/white_sheep.png'), 1/10)


    #Sliders
    ###############################################

    #Grass Growth Rate (ggr)
    #############################

    app.ggrSliding = False
    app.ggrNum = 5

    app.ggrTextX = app.width/1.65
    app.ggrTextY = app.margin

    app.ggrLineTopX = app.ggrTextX - 100
    app.ggrLineTopY = app.ggrTextY + 30
    app.ggrLineBottomX = app.ggrTextX + 100
    app.ggrLineBottomY = app.ggrLineTopY
    app.ggrLineLength = app.ggrLineBottomX - app.ggrLineTopX

    app.ggrSliderTopX = app.ggrLineTopX + (app.ggrLineLength/2) - 4
    app.ggrSliderTopY = app.ggrLineTopY - 10
    app.ggrSliderBottomX = app.ggrSliderTopX + 8
    app.ggrSliderBottomY = app.ggrLineTopY + 10

    #Water Fall Rate (wfr)
    #############################

    app.wfrSliding = False
    app.wfrNum = 5

    app.wfrTextX = app.width/1.3
    app.wfrTextY = app.margin

    app.wfrLineTopX = app.wfrTextX - 100
    app.wfrLineTopY = app.wfrTextY + 30
    app.wfrLineBottomX = app.wfrTextX + 100
    app.wfrLineBottomY = app.wfrLineTopY
    app.wfrLineLength = app.wfrLineBottomX - app.wfrLineTopX

    app.wfrSliderTopX = app.wfrLineTopX + (app.wfrLineLength/2) - 4
    app.wfrSliderTopY = app.wfrLineTopY - 10
    app.wfrSliderBottomX = app.wfrSliderTopX + 8
    app.wfrSliderBottomY = app.wfrLineTopY + 10


######################################################################
#Title Screen
######################################################################

def titleScreen_redrawAll(app, canvas):
    canvas.create_text(app.width//2, app.height/5, text="EcoSim", fill="black", font="Ariel 100")
    canvas.create_rectangle(app.width/2.5, app.height/1.9, app.width/1.65, app.height/2.3, fill='black')
    canvas.create_text(app.width//2, app.height/2.1, text="Enter Simulation", fill='white', font='Ariel 40')
    canvas.create_text(app.width//2, app.height/1.025, text="Created by Eli Slothower, Carnegie Mellon University class of 2025", fill='black', font='Ariel 20')

def titleScreen_mousePressed(app, event):
    topLeftXTitleScreen = app.width/2.5
    topLeftYTitleScreen = app.height/1.9
    bottomRightXTitleScreen = app.width/1.65
    bottomRightYTitleScreen = app.height/2.3

    if(topLeftXTitleScreen < event.x < bottomRightXTitleScreen and bottomRightYTitleScreen < event.y < topLeftYTitleScreen):
        app.mode = 'simulateScreen'

######################################################################
#Drawing grid
######################################################################

def getCellColorsList(app, rows, cols):
    cellColorsList = [['green' for _ in range(app.rows)] for _ in range(app.cols)]
    cellColorsList = getAddedWaterList(app, cellColorsList)
    cellColorsList = getAddedFlowersList(app, cellColorsList)
    cellColorsList = getAddedBareSpotsList(app, cellColorsList)
    return cellColorsList

def getCellBounds(app, row, col):


    x0 = app.margin + app.gridWidth * col / app.cols
    x1 = app.margin + app.gridWidth * (col+1) / app.cols
    y0 = app.margin + app.gridHeight * row / app.rows
    y1 = app.margin + app.gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def getAddedBareSpotsList(app, currentCellColorsList):

    numberOfBareSpots = random.randrange(5, (app.rows*app.cols)//8)

    for _ in range(numberOfBareSpots + 1):
        row = random.randrange(app.rows)
        col = random.randrange(app.cols)
        if currentCellColorsList[row][col] in ['blue', 'pink', 'red', 'purple', 'yellow', 'orange']:
            continue
        else:
            currentCellColorsList[row][col] = 'tan'

    return currentCellColorsList


def getAddedFlowersList(app, currentCellColorsList):

    numberOfFlowers = random.randrange(5, (app.rows*app.cols)//40)

    for _ in range(numberOfFlowers + 1):
        flowerColor = app.flowerColorOptions[random.randrange(0,5)]
        row = random.randrange(app.rows)
        col = random.randrange(app.cols)

        if currentCellColorsList[row][col] == 'blue':
            continue
        else:
            currentCellColorsList[row][col] = flowerColor

    return currentCellColorsList

def getAddedWaterList(app, currentCellColorsList):

    numberOfBodiesOfWater = random.randrange(0,3)
    
    for bodyOfWater in range(numberOfBodiesOfWater + 1):
        layersOfWater = random.randrange(3,7)
        row = random.randrange(app.rows)
        col = random.randrange(app.cols)

        currentCellColorsList[row][col] = 'blue'

        
        for drow in [-1, 0, +1]:
            for dcol in [-1, 0, +1]: 
                if (drow, dcol) != (0, 0):
                    for layer in range(layersOfWater + 1):
                        rowBeingChecked = row + layer*drow
                        colBeingChecked = col + layer*dcol

                        if ((rowBeingChecked < 0) or (rowBeingChecked >= app.rows) or (colBeingChecked < 0) or (colBeingChecked >= app.cols)):
                            continue
                        else:
                            currentCellColorsList[rowBeingChecked][colBeingChecked] = 'blue'

                            for drowTwo in [-1, 0, +1]:
                                for dcolTwo in [-1, 0, +1]: 
                                    if (drowTwo, dcolTwo) != (0, 0):
                                        for layerTwo in range(2):
                                            rowBeingCheckedTwo = rowBeingChecked + layerTwo*drowTwo
                                            colBeingCheckedTwo = colBeingChecked + layerTwo*dcolTwo

                                            if ((rowBeingCheckedTwo < 0) or (rowBeingCheckedTwo >= app.rows) or (colBeingCheckedTwo < 0) or (colBeingCheckedTwo >= app.cols)):
                                                continue
                                            else:
                                                currentCellColorsList[rowBeingCheckedTwo][colBeingCheckedTwo] = 'blue'

                                                if bodyOfWater == numberOfBodiesOfWater:
                                                    chance = random.randrange(2)
                                                    if chance == 0:
                                                        currentCellColorsList[rowBeingCheckedTwo][colBeingCheckedTwo] = 'blue'
                                                else:
                                                    currentCellColorsList[rowBeingChecked][colBeingChecked] = 'blue'

                                                    # for drowThree in [-1, 0, +1]:
                                                    #     for dcolThree in [-1, 0, +1]: 
                                                    #         if (drowThree, dcolThree) != (0, 0):
                                                    #             for layerThree in range(2):
                                                    #                 rowBeingCheckedThree = rowBeingCheckedTwo + layerThree*drowThree
                                                    #                 colBeingCheckedThree = colBeingCheckedTwo + layerTwo*dcolThree

                                                    #                 if ((rowBeingCheckedThree < 0) or (rowBeingCheckedThree >= app.rows) or (colBeingCheckedThree < 0) or (colBeingCheckedThree >= app.cols)):
                                                    #                     continue
                                                    #                 else:
                                                    #                     currentCellColorsList[rowBeingCheckedThree][colBeingCheckedThree] = 'blue'

                                                    #                     if bodyOfWater == numberOfBodiesOfWater:
                                                    #                         chance = random.randrange(2)
                                                    #                         if chance == 0:
                                                    #                             currentCellColorsList[rowBeingCheckedThree][colBeingCheckedThree] = 'blue'
                                                    #                     else:
                                                    #                         currentCellColorsList[rowBeingCheckedTwo][colBeingCheckedTwo] = 'blue'
    return currentCellColorsList


def drawSheep(app, canvas):

    for sheep in range(len(SheepNames)): #display sheep after wolves because sheep are smaller. This ensures user can see sheep (unless size mutation of wolf, for example)
        canvas.create_image(SheepPosition[sheep][0], SheepPosition[sheep][1], image=ImageTk.PhotoImage(app.sheepImage)) 



def moveWolvesTowardSheep(wolf, app, canvas):
    currentWolfPositionRow = WolfPosition[wolf][0]
    currentWolfPositionCol = WolfPosition[wolf][1]
    foundMove = False

    #WolfPosition[wolf][0] += random.randrange(-5,5)
    #WolfPosition[wolf][1] += random.randrange(-5,5)
    #print(WolfPosition)


    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]: 
            if foundMove: break
            
            elif (drow, dcol) != (0, 0):
                for i in range(-200, 200):
                    rowBeingChecked = currentWolfPositionRow + i*drow
                    colBeingChecked = currentWolfPositionCol + i*dcol

                    #print(f"[{rowBeingChecked}, {colBeingChecked}]")

                    if [rowBeingChecked, colBeingChecked] in SheepPosition:
                        

                        # if [WolfPosition[wolf][0], WolfPosition[wolf][1]] in SheepPosition:
                        #     WolfPosition[wolf][0] = rowBeingChecked
                        #     WolfPosition[wolf][1] = colBeingChecked
                            # print("ATE THE SHEEP", random.randint(0,100))
                            # foundMove = True
                        
                            # break
                        
                        if rowBeingChecked - WolfPosition[wolf][0] < 1 or colBeingChecked - WolfPosition[wolf][1] < 1:
                            print("ATE THE SHEEP", random.randint(0,100))
                            foundMove = True
                        
                            break
                        
                        else:
                            WolfPosition[wolf][0] += (rowBeingChecked - WolfPosition[wolf][0])/5
                            WolfPosition[wolf][1] += (colBeingChecked - WolfPosition[wolf][1])/5
                            print("IT", random.randint(0,100))

                        
            

        if foundMove: break                   
        for _ in range(random.randrange(0,200)):
            newWolfRow =  WolfPosition[wolf][0] + random.randrange(-1,2)
            newWolfCol = WolfPosition[wolf][1] + random.randrange(-1,2)

            if app.margin + 12 < newWolfRow < app.gridWidth + 12 and app.margin + 12 < newWolfCol < app.gridHeight + 12:
                WolfPosition[wolf][0] = newWolfRow
                WolfPosition[wolf][1] = newWolfCol





def drawWolves(app, canvas):

    for wolf in range(len(WolfNames)): 
        moveWolvesTowardSheep(wolf, app, canvas)
        canvas.create_image(WolfPosition[wolf][0], WolfPosition[wolf][1], image=ImageTk.PhotoImage(app.wolfImage))  


def drawBoard(app, canvas):   
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.cellColorsList[row][col]
            drawCell(app, canvas, row, col, color)

def drawCell(app, canvas, row, col, color):
    (x0, y0, x1, y1) = getCellBounds(app, row, col)
    
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width = 1)

def simulateScreen_redrawAll(app, canvas):

    #Draws terrain with border
    canvas.create_rectangle(app.margin, app.margin, (app.width//2) + app.margin, app.height-app.margin, outline='black', width=20)
    drawBoard(app, canvas)

    drawWolves(app, canvas)
    drawSheep(app, canvas)

    canvas.create_text(app.ggrTextX, app.ggrTextY, text=f"Grass Growth Rate: {app.ggrNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.ggrLineTopX, app.ggrLineTopY, app.ggrLineBottomX, app.ggrLineBottomY, fill='grey', width=3)
    canvas.create_rectangle(app.ggrSliderTopX, app.ggrSliderTopY, app.ggrSliderBottomX, app.ggrSliderBottomY, fill='black')

    canvas.create_text(app.wfrTextX, app.wfrTextY, text=f"Water Fall Rate: {app.wfrNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.wfrLineTopX, app.wfrLineTopY, app.wfrLineBottomX, app.wfrLineBottomY, fill='grey', width=3)
    canvas.create_rectangle(app.wfrSliderTopX, app.wfrSliderTopY, app.wfrSliderBottomX, app.wfrSliderBottomY, fill='black')

def simulateScreen_mouseReleased(app, event): 
    app.ggrSliding = False
    app.wfrSliding = False

def simulateScreen_mousePressed(app, event):
    if app.ggrSliderTopX <= event.x <= app.ggrSliderBottomX and app.ggrSliderTopY < event.y < app.ggrSliderBottomY:
        app.ggrSliding = True

    if app.wfrSliderTopX <= event.x <= app.wfrSliderBottomX and app.wfrSliderTopY < event.y < app.wfrSliderBottomY:
        app.wfrSliding = True


def simulateScreen_mouseDragged(app, event): 
    print("Dragging")

    #Logic for Grass Growth Rate (ggr) slider
    ################################################
    if app.ggrSliderTopX <= event.x <= app.ggrSliderBottomX and app.ggrSliderTopY < event.y < app.ggrSliderBottomY:
        app.ggrSliding = True

    if app.ggrSliding and app.ggrLineTopX < event.x < app.ggrLineBottomX:
        app.ggrSliderTopX = event.x
        app.ggrSliderBottomX = app.ggrSliderTopX + 8
    elif app.ggrSliding and event.x < app.ggrLineTopX:
        app.ggrSliderTopX = app.ggrLineTopX
        app.ggrSliderBottomX = app.ggrSliderTopX + 8
    elif app.ggrSliding and app.ggrLineBottomX < event.x:
        app.ggrSliderTopX = app.ggrLineBottomX
        app.ggrSliderBottomX = app.ggrSliderTopX + 8

    app.ggrNum = int(((app.ggrSliderTopX-app.ggrLineTopX)/app.ggrLineLength)*10)

    #1-10 as the scale is more readable for users, rather than 0-9
    if app.ggrNum == 0: app.ggrNum = 1
    elif app.ggrNum == 9: app.ggrNum = 10


    #Logic for Water Fall Rate (wfr) slider
    ################################################

    if app.wfrSliderTopX <= event.x <= app.wfrSliderBottomX and app.wfrSliderTopY < event.y < app.wfrSliderBottomY:
        app.wfrSliding = True

    if app.wfrSliding and app.wfrLineTopX < event.x < app.wfrLineBottomX:
        app.wfrSliderTopX = event.x
        app.wfrSliderBottomX = app.wfrSliderTopX + 8
    elif app.wfrSliding and event.x < app.wfrLineTopX:
        app.wfrSliderTopX = app.wfrLineTopX
        app.wfrSliderBottomX = app.wfrSliderTopX + 8
    elif app.wfrSliding and app.wfrLineBottomX < event.x:
        app.wfrSliderTopX = app.wfrLineBottomX
        app.wfrSliderBottomX = app.wfrSliderTopX + 8

    app.wfrNum = int(((app.wfrSliderTopX-app.wfrLineTopX)/app.wfrLineLength)*10)

    #1-10 as the scale is more readable for users, rather than 0-9
    if app.wfrNum == 0: app.wfrNum = 1
    elif app.wfrNum == 9: app.wfrNum = 10


runApp(width=1728, height=905)

######################################################################
#Testing
######################################################################

from matplotlib import pyplot as plt
import numpy as np

xValues = [0,1,2,3,4,5]
yValues = [0,6,25,4,6,2]

otherXValues = [0,12,15,20,24,28]
otherYValues = [0,25, 25, 8, 1, 14]

plt.scatter(xValues, yValues)
plt.plot(xValues, yValues, 'red',
        otherXValues, otherYValues, 'purple')



plt.title("Sample Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.axis([0,30,0,42]) #changes the axis points, x values go from 0-30, y values go from 0-42


for i in range(4):
    plt.plot(np.random.rand(10))

#plt.show()