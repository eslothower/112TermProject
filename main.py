#Created by Eli Slothower (Andrew ID: eslothow)

#main.py is the primary file containing most of the code used for EcoSim.
#It contains the code for the following processes:
#   - Terrain Generation
#   - User input (i.e. the sliders), which directly impacts the simulation
#   - The custom-built graph which displays the current populations for each 
#     animal type (i.e. sheep and wolves)
#   - Animal attribute modifications (i.e., when it's time to give birth to 
#     offspring, or when an animal's health decreases since they haven't 
#     eaten in awhile, etc)
#   - Animal movement (i.e. when the wolves track the sheep)
#   - The drawing of the canvases (i.e. the title screen and the sim screen)

######################################################################
#Imports
######################################################################

from cmu_112_graphics import *
from Animal import *
from Sheep import *
from Wolf import *
import random
import decimal

#from the HW assignments on https://www.cs.cmu.edu/~112/index.html
def roundHalfUp(d): #helper-fn
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

######################################################################
#Animal Code
######################################################################

#The default amount for each animal type
wolfCount = 5
sheepCount = 5

#A dictionary that keeps track of how many animals are 'alive' at once 
#(i.e. on the screen)
animalCount = {'Wolf': wolfCount, 'Sheep': sheepCount}


SheepNames = []
WolfNames = []

#Keeps track of all the current 'alive' animals' positions on the grid
SheepPosition = []
WolfPosition = []


#Initializes each animal instance with a unique name, provides them a position 
#on the grid
def initializeAnimals(app):

    #Global variables... I know. This is necessary though because I need to 
    #access these variables in certain functions that do not have access to the 
    #attribute 'app'. This is why I cannot make these variables an 'app.' var.
    global SheepNames
    global WolfNames
    global SheepPosition 
    global WolfPosition

    SheepNames = []
    WolfNames = []
    SheepPosition = []
    WolfPosition = []

    for key in animalCount:
        for _ in range(animalCount[key]):
            
            while True:

                #a random number to put at the end of the instance's name
                #(i.e. 'wolf8349'). This ensures a unique name for each instance
                number = random.randrange(1000000000000)

                #Creates a name with the animal type and number combined based
                #off of the key of the dictionary, as well as the random number
                animalName = '%s%s' % ([key], number)

                if animalName not in globals()[key+'Names']:
                    
                    #Adds unique name to respective set
                    #i.e. SheepNames or WolfNames
                    #This ensures there will never be more than one instance 
                    #with the same name
                    globals()[key+'Names'].append(animalName)

                    #Actually initializes animal instance
                    #i.e. wolf1 = Wolf()
                    if key == 'Sheep':
                        globals()[animalName] = eval(key+'(offspringRate=50, health=100)')  
                    elif key == 'Wolf':
                        globals()[animalName] = eval(key+'(offspringRate=150, health=250)')  

                    #Creates a random position that is not in water for the animal
                    row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)

                    while app.cellColorsList[row][col] == 'blue':

                        row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)

                    globals()[key+'Position'].append([row, col])
                    break

######################################################################
#App Started
######################################################################

def appStarted(app):

    #System Settings
    ###############################################

    app.mode = "titleScreen"
    app._root.resizable(False, False) #Contributed by Anita (TA) on Piazza @4354
    app.timerDelay = 90 
    app.runSim = False #signifies whether the sim is running or not

    #used for when the sim is paused
    app.stockSimWithOverlayWithTextImage = app.scaleImage(app.loadImage(
                'assets/Modified/stockSimWithOverlayWithTextImage.png'), 1/2.04)

    #Code for grid/terrain generation
    ###############################################
    app.rows = 30
    app.cols = 30
    app.cellSize = 25
    app.margin = 25
    app.gridWidth  = app.width//2 #this makes the grid go to the left side
    app.gridHeight = app.height - 2*app.margin
    app.colors = ['green', 'tan', 'blue']
    app.waterPuddles = random.randrange(3)
    app.waterAmount = 'Regular'
    app.flowerColorOptions = ['pink', 'red', 'purple', 'yellow', 'orange']
    

    #Code for animal images
    ###############################################
    app.wolfImage = app.scaleImage(app.loadImage(
                                        'assets/Modified/black_wolf.png'), 1/10)
    app.mutatedLargeWolfImage = app.scaleImage(app.loadImage(
                                         'assets/Modified/black_wolf.png'), 1/7)
    app.sheepImage = app.scaleImage(app.loadImage(
                                       'assets/Modified/white_sheep.png'), 1/10)
    app.mutatedPurpleSheepImage = app.scaleImage(app.loadImage(
                                        'assets/Modified/purple_sheep.png'), 1/10)


    #Sliders
    ###############################################

    #Grass Growth Rate (ggr)
    #############################

    app.ggrSliding = False
    app.ggrNum = 5

    #Label
    app.ggrTextX = app.width/1.65
    app.ggrTextY = app.margin

    #Slider Line
    app.ggrLineTopX = app.ggrTextX - 100
    app.ggrLineTopY = app.ggrTextY + 30
    app.ggrLineBottomX = app.ggrTextX + 100
    app.ggrLineBottomY = app.ggrLineTopY
    app.ggrLineLength = app.ggrLineBottomX - app.ggrLineTopX

    #Slider Box
    app.ggrSliderTopX = app.ggrLineTopX + (app.ggrLineLength/2) - 4
    app.ggrSliderTopY = app.ggrLineTopY - 10
    app.ggrSliderBottomX = app.ggrSliderTopX + 8
    app.ggrSliderBottomY = app.ggrLineTopY + 10

    #Average Amount of Water (aaw)
    #############################

    app.aawSliding = False
    app.aawNum = 2

    #Label
    app.aawTextX = app.width/1.3
    app.aawTextY = app.margin

    #Slider Line
    app.aawLineTopX = app.aawTextX - 100
    app.aawLineTopY = app.aawTextY + 30
    app.aawLineBottomX = app.aawTextX + 100
    app.aawLineBottomY = app.aawLineTopY
    app.aawLineLength = app.aawLineBottomX - app.aawLineTopX

    #Slider Box
    app.aawSliderTopX = app.aawLineTopX + (app.aawLineLength/2) - 4
    app.aawSliderTopY = app.aawLineTopY - 10
    app.aawSliderBottomX = app.aawSliderTopX + 8
    app.aawSliderBottomY = app.aawLineTopY + 10

    #Starting Wolf Population (swp)
    #############################

    app.swpSliding = False
    app.swpNum = 5

    #Label
    app.swpTextX = app.width/1.65
    app.swpTextY = app.height/4

    #Slider Line
    app.swpLineTopX = app.swpTextX - 100
    app.swpLineTopY = app.swpTextY + 30
    app.swpLineBottomX = app.swpTextX + 100
    app.swpLineBottomY = app.swpLineTopY
    app.swpLineLength = app.swpLineBottomX - app.swpLineTopX

    #Slider Box
    app.swpSliderTopX = app.swpLineTopX + (app.swpLineLength/2) - 4
    app.swpSliderTopY = app.swpLineTopY - 10
    app.swpSliderBottomX = app.swpSliderTopX + 8
    app.swpSliderBottomY = app.swpLineTopY + 10

    #Starting Sheep Population (ssp)
    #############################

    app.sspSliding = False
    app.sspNum = 5

    #Label
    app.sspTextX = app.width/1.3
    app.sspTextY = app.height/4

    #Slider Line
    app.sspLineTopX = app.sspTextX - 100
    app.sspLineTopY = app.sspTextY + 30
    app.sspLineBottomX = app.sspTextX + 100
    app.sspLineBottomY = app.sspLineTopY
    app.sspLineLength = app.sspLineBottomX - app.sspLineTopX

    #Slider Box
    app.sspSliderTopX = app.sspLineTopX + (app.sspLineLength/2) - 4
    app.sspSliderTopY = app.sspLineTopY - 10
    app.sspSliderBottomX = app.sspSliderTopX + 8
    app.sspSliderBottomY = app.sspLineTopY + 10

    #Flower Growth Rate (fgr)
    #############################

    app.fgrSliding = False
    app.fgrNum = 5

    #Label
    app.fgrTextX = app.width/1.08
    app.fgrTextY = app.margin

    #Slider Line
    app.fgrLineTopX = app.fgrTextX - 100
    app.fgrLineTopY = app.fgrTextY + 30
    app.fgrLineBottomX = app.fgrTextX + 100
    app.fgrLineBottomY = app.fgrLineTopY
    app.fgrLineLength = app.fgrLineBottomX - app.fgrLineTopX

    #Slider Box
    app.fgrSliderTopX = app.fgrLineTopX + (app.fgrLineLength/2) - 4
    app.fgrSliderTopY = app.fgrLineTopY - 10
    app.fgrSliderBottomX = app.fgrSliderTopX + 8
    app.fgrSliderBottomY = app.fgrLineTopY + 10

    #Requires variables from above, so must go here
    app.cellColorsList = getCellColorsList(app)  

######################################################################
#Terrain Generation
######################################################################

#creates a 2D list that represents the terrain in grid-form
def getCellColorsList(app):
    cellColorsList = [['green' for _ in range(app.rows)] for _ in range(app.cols)]
    cellColorsList = getAddedBareSpotsList(app, cellColorsList)
    cellColorsList = getAddedWaterList(app, cellColorsList)
    cellColorsList = getAddedFlowersList(app, cellColorsList)
    
    return cellColorsList

#Adds bare spots to the terrain
def getAddedBareSpotsList(app, currentCellColorsList):

    #Changes the amount of bare spots added depending on the slider (user input)
    if app.ggrNum == 10:
        numberOfBareSpots = 0
    elif app.ggrNum == 9:
        numberOfBareSpots = (app.rows*app.cols)//100
    elif app.ggrNum == 8:
        numberOfBareSpots = (app.rows*app.cols)//40
    elif app.ggrNum == 7:
        numberOfBareSpots = (app.rows*app.cols)//15
    elif app.ggrNum == 6:
        numberOfBareSpots = (app.rows*app.cols)//10
    elif app.ggrNum == 5:
        numberOfBareSpots = (app.rows*app.cols)//7
    elif app.ggrNum == 4:
        numberOfBareSpots = (app.rows*app.cols)//4
    elif app.ggrNum == 3:
        numberOfBareSpots = (app.rows*app.cols)//2
    elif app.ggrNum == 2:
        numberOfBareSpots = roundHalfUp((app.rows*app.cols)/1.2)
    elif app.ggrNum == 1:
        numberOfBareSpots = (app.rows*app.cols)

    #Makes the cells tan according to the numberOfBareSpots
    if app.ggrNum == 1:
        currentCellColorsList = [['tan' for _ in range(app.rows)] for _ in range(app.cols)]
    else:
        for _ in range(numberOfBareSpots + 1):
            row = random.randrange(app.rows)
            col = random.randrange(app.cols)

            currentCellColorsList[row][col] = 'tan'

    return currentCellColorsList

#Adds flowers to the terrain
def getAddedFlowersList(app, currentCellColorsList):

    #Changes the amount of flowers added depending on the slider (user input)
    if app.fgrNum == 10:
        numberOfFlowers = 150
    elif app.fgrNum == 9:
        numberOfFlowers = 110
    elif app.fgrNum == 8:
        numberOfFlowers = 80
    elif app.fgrNum == 7:
        numberOfFlowers = 65
    elif app.fgrNum == 6:
        numberOfFlowers = 45
    elif app.fgrNum == 5:
        numberOfFlowers = 35
    elif app.fgrNum == 4:
        numberOfFlowers = 20
    elif app.fgrNum == 3:
        numberOfFlowers = 10
    elif app.fgrNum == 2:
        numberOfFlowers = 5
    elif app.fgrNum == 1:
        numberOfFlowers = 2

    #Makes the cells a random flowerColor according to the numberOfFlowers
    for _ in range(numberOfFlowers + 1):
        flowerColor = app.flowerColorOptions[random.randrange(0,5)]
        row = random.randrange(app.rows)
        col = random.randrange(app.cols)

        if currentCellColorsList[row][col] == 'blue':
            continue
        else:
            currentCellColorsList[row][col] = flowerColor

    return currentCellColorsList

#Adds bodies of water to the terrain
def getAddedWaterList(app, currentCellColorsList):
    numberOfBodiesOfWater = app.aawNum
    
    for bodyOfWater in range(numberOfBodiesOfWater):
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

    return currentCellColorsList

######################################################################
#Animal movement
######################################################################

#Moves sheep in a semi-random order, ensuring that they don't move into a sheep
def moveSheep(row, col, app):

    drow = random.randrange(-1, 2) #-1, 0, or 1
    dcol = random.randrange(-1, 2) #-1, 0, or 1

    while ((not(0 <= row + drow <= app.rows - 1)) or 
          (not (0 <= col + dcol <= app.cols - 1)) or 
          ([row + drow, col + dcol] in WolfPosition)): #sheep won't step into a wolf

        drow = random.randrange(-1, 2) #-1, 0, or 1
        dcol = random.randrange(-1, 2) #-1, 0, or 1

    return [row + drow, col + dcol]

#Enables wolves to track sheep positions, then move towards sheep
def moveWolvesTowardSheep(row, col, app):

    foundSheep = False
    originalRow = row
    originalCol = col
    tempRow = row
    tempCol = col
    

    while foundSheep == False:
        
        if len(SheepPosition) > 0:

            #The two following ranges define how large the radius is for the 
            #wolve's sheep-detection. The larger these two ranges are, the 
            #further the wolves can detect the sheep
            for drow in range(-8, 8):
                for dcol in range(-8, 8):
                    if (drow, dcol) != (0, 0):

                        #Code that tracks the sheep positions
                        #We don't have to check whether or not the new row/col 
                        #is within the bounds of the grid or not because we do it 
                        #already with the sheep. Therefore, if this boolean is True,
                        #then we already know it's a valid move
                        if [tempRow + drow, tempCol + dcol] in SheepPosition:
                            foundSheep = True

                            if drow > 0 and dcol > 0:
                                return [originalRow + 1, originalCol + 1]
                            elif drow == 0 and dcol > 0:
                                return [originalRow, originalCol + 1] 
                            elif drow > 0 and dcol == 0:
                                return [originalRow + 1, originalCol]
                            elif drow < 0 and dcol < 0:
                                return [originalRow - 1, originalCol - 1]
                            elif drow == 0 and dcol < 0:
                                return [originalRow, originalCol - 1]
                            elif drow < 0 and dcol == 0:
                                return [originalRow - 1, originalCol]
                            elif drow > 0 and dcol < 0:
                                return [originalRow + 1, originalCol - 1]
                            elif drow < 0 and dcol > 0:
                                return [originalRow - 1, originalCol + 1]

        #Changes the wolves' direction according to where the nearest sheep is
        newDrow = random.randrange(-1, 2) #-1, 0, or 1
        newDcol = random.randrange(-1, 2) #-1, 0, or 1

        while ((not(0 <= row + newDrow <= app.rows - 1)) or 
            (not (0 <= col + newDcol <= app.cols - 1)) or 
            ([row + newDrow, col + newDcol] in WolfPosition)): #wolf won't step into a wolf

            newDrow = random.randrange(-1, 2) #-1, 0, or 1
            newDcol = random.randrange(-1, 2) #-1, 0, or 1

        return [row + newDrow, col + newDcol]

######################################################################
#Draws grid
######################################################################

def getCellBounds(app, row, col):

    x0 = app.margin + app.gridWidth * col / app.cols
    x1 = app.margin + app.gridWidth * (col+1) / app.cols
    y0 = app.margin + app.gridHeight * row / app.rows
    y1 = app.margin + app.gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def drawCell(app, canvas, row, col, color):

    (x0, y0, x1, y1) = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width = 1)

def drawBoard(app, canvas):  

    canvas.create_rectangle(app.margin, app.margin, (app.width//2) + app.margin, app.height-app.margin, outline='black', width=20)
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.cellColorsList[row][col]
            drawCell(app, canvas, row, col, color)

######################################################################
#Draws animals
######################################################################

def drawWolves(app, canvas):

    for i in range(len(WolfPosition)):
        [row, col] = WolfPosition[i]
        [row, col] = moveWolvesTowardSheep(row, col, app)
        WolfPosition[i] = [row, col]

        #delete the sheep because the sheep was EATEN!
        for w in range(len(SheepPosition)):
            if SheepPosition[w] == [row, col]: 
                SheepPosition.pop(w)
                SheepNames.pop(w)
                globals()[WolfNames[i]].eatSheep()
                break

        #we don't need x1 and y1
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        x0 += 15
        y0 += 13
        canvas.create_image(x0, y0, image=ImageTk.PhotoImage(app.wolfImage)) 

        #handles drawing different wolf based of off mutations
        currentWolf = WolfNames[i]

        if globals()[currentWolf].getMutationType() == 0:
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(app.wolfImage))

        elif globals()[currentWolf].getMutationType() == 1:
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(app.mutatedLargeWolfImage))

def drawSheep(app, canvas):

    for i in range(len(SheepPosition)):
        [row, col] = SheepPosition[i]
        [row, col] = moveSheep(row, col, app)
        SheepPosition[i] = [row, col]
        #we don't need x1 and y1
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        x0 += 15
        y0 += 13
        
        #handles drawing different sheep based of off mutations
        currentSheep = SheepNames[i]

        if globals()[currentSheep].getMutationType() == 0:
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(app.sheepImage))

        elif globals()[currentSheep].getMutationType() == 1:
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(app.mutatedPurpleSheepImage))

        if globals()[currentSheep].getCurrentHungerLevel() > 0:
            if app.cellColorsList[row][col] == 'green':
                app.cellColorsList[row][col] = 'tan'
                globals()[currentSheep].eatGrass()
            if app.cellColorsList[row][col] in app.flowerColorOptions:
                app.cellColorsList[row][col] = 'tan'
                globals()[currentSheep].eatFlower()

######################################################################
#Draws sliders
######################################################################

def drawGrassGrowthRateSlider(app, canvas):
    canvas.create_text(app.ggrTextX, app.ggrTextY, text=f"Grass Growth Rate: {app.ggrNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.ggrLineTopX, app.ggrLineTopY, app.ggrLineBottomX, app.ggrLineBottomY, fill='grey', width=3)

    #Greys out sliders when the sim is running to signify that the slider cannot be used while the sim is running
    if app.runSim:
        canvas.create_rectangle(app.ggrSliderTopX, app.ggrSliderTopY, app.ggrSliderBottomX, app.ggrSliderBottomY, fill='#cfcfcf')
    else:
        canvas.create_rectangle(app.ggrSliderTopX, app.ggrSliderTopY, app.ggrSliderBottomX, app.ggrSliderBottomY, fill='black')

def drawWaterFallRateSlider(app, canvas):
    canvas.create_text(app.aawTextX, app.aawTextY, text=f"Average Amount of Water: {app.aawNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.aawLineTopX, app.aawLineTopY, app.aawLineBottomX, app.aawLineBottomY, fill='grey', width=3)

    #Greys out sliders when the sim is running to signify that the slider cannot be used while the sim is running
    if app.runSim:
        canvas.create_rectangle(app.aawSliderTopX, app.aawSliderTopY, app.aawSliderBottomX, app.aawSliderBottomY, fill='#cfcfcf')
    else:
        canvas.create_rectangle(app.aawSliderTopX, app.aawSliderTopY, app.aawSliderBottomX, app.aawSliderBottomY, fill='black')

def drawStartingWolfPopulationSlider(app, canvas):
    canvas.create_text(app.swpTextX, app.swpTextY, text=f"Starting Wolf Population: {app.swpNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.swpLineTopX, app.swpLineTopY, app.swpLineBottomX, app.swpLineBottomY, fill='grey', width=3)

    #Greys out sliders when the sim is running to signify that the slider cannot be used while the sim is running
    if app.runSim:
        canvas.create_rectangle(app.swpSliderTopX, app.swpSliderTopY, app.swpSliderBottomX, app.swpSliderBottomY, fill='#cfcfcf')
    else:
        canvas.create_rectangle(app.swpSliderTopX, app.swpSliderTopY, app.swpSliderBottomX, app.swpSliderBottomY, fill='black')

def drawStartingSheepPopulationSlider(app, canvas):
    canvas.create_text(app.sspTextX, app.sspTextY, text=f"Starting Sheep Population: {app.sspNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.sspLineTopX, app.sspLineTopY, app.sspLineBottomX, app.sspLineBottomY, fill='grey', width=3)

    #Greys out sliders when the sim is running to signify that the slider cannot be used while the sim is running
    if app.runSim: 
        canvas.create_rectangle(app.sspSliderTopX, app.sspSliderTopY, app.sspSliderBottomX, app.sspSliderBottomY, fill='#cfcfcf')
    else:
        canvas.create_rectangle(app.sspSliderTopX, app.sspSliderTopY, app.sspSliderBottomX, app.sspSliderBottomY, fill='black')

def drawFlowerGrowthRateSlider(app, canvas):
    canvas.create_text(app.fgrTextX, app.fgrTextY, text=f"Flower Growth Rate: {app.fgrNum}", fill='black', font='Ariel 18')
    canvas.create_line(app.fgrLineTopX, app.fgrLineTopY, app.fgrLineBottomX, app.fgrLineBottomY, fill='grey', width=3)

    #Greys out sliders when the sim is running to signify that the slider cannot be used while the sim is running
    if app.runSim:
        canvas.create_rectangle(app.fgrSliderTopX, app.fgrSliderTopY, app.fgrSliderBottomX, app.fgrSliderBottomY, fill='#cfcfcf')
    else:
        canvas.create_rectangle(app.fgrSliderTopX, app.fgrSliderTopY, app.fgrSliderBottomX, app.fgrSliderBottomY, fill='black')

######################################################################
#Draws graph
######################################################################

def drawGraph(app, canvas):
    canvas.create_rectangle(app.width/1.845, app.height/1.7, app.width - app.margin + 10, app.height/1.12, outline='black')
    canvas.create_text(app.width/1.875, app.height/1.12, text='0', fill='black')
    canvas.create_text(app.width/1.87, app.height/1.23, text='5', fill='black')
    canvas.create_text(app.width/1.87, app.height/1.34, text='10', fill='black')
    canvas.create_text(app.width/1.87, app.height/1.49, text='15', fill='black')
    canvas.create_text(app.width/1.87, app.height/1.7, text='20+', fill='black')

    firstRun = True
    for key in animalCount:

        if firstRun:
            canvas.create_line(app.width/1.845, app.height/1.12, app.width/1.6, app.height/1.15, fill='red', width=4)

######################################################################
#Title Screen Logic
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
#Simulate Screen Logic
######################################################################

def simulateScreen_timerFired(app):

    wolvesToBeBorn = 0
    wolvesThatGaveBirth = 0

    #Declares that new offspring will be born whenever offspringCounter is 
    #equal to that specific animal instance's offspringRate (as each animal 
    #instance could have a different offspringRate due to species and/or mutation)
    #Also handles starvation, which declines animal instance's health and eventually
    #kills the animal instance (unless there is always a supply of food, keeping)
    #the hunger levels down and the health levels up
    for wolf in range(len(WolfNames)):
        
        offspringCounter = globals()[WolfNames[wolf]].getOffspringCounter()
        offspringRate = globals()[WolfNames[wolf]].getOffspringRate() 

        if offspringCounter < offspringRate:
            globals()[WolfNames[wolf]].addOneToOffspringCounter()
            
        else:
            if wolvesThatGaveBirth < len(WolfPosition):
                wolvesToBeBorn += 1
            
            globals()[WolfNames[wolf]].resetOffspringCounter()

        
        currentWolfHealth = globals()[WolfNames[wolf]].getCurrentHealth()
        currentWolfHungerLevel = globals()[WolfNames[wolf]].getCurrentHungerLevel()
        print("Current Wolf Health:", currentWolfHealth)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
        if currentWolfHungerLevel < 100:
            globals()[WolfNames[wolf]].getHungrier()
        else:
            globals()[WolfNames[wolf]].loseHealth()
            currentWolfHealth = globals()[WolfNames[wolf]].getCurrentHealth()
            print("Current Wolf Health:", currentWolfHealth)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
            print("Current Wolf hunger:", currentWolfHungerLevel)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
        
        if currentWolfHealth <= 0:
            WolfNames.pop(wolf)
            WolfPosition.pop(wolf)
            break

        


    #Caps combined animal population at 150 to ensure good performance
    if len(WolfPosition) + len(SheepPosition) < 150:
    
        #Initializes new wolf offspring
        for _ in range(wolvesToBeBorn):

            number = random.randrange(1000000000000)
            animalName = '%s%s' % ('Wolf', number)
            if animalName not in globals()['WolfNames']:
                
                #Adds unique name to respective set
                #i.e. SheepNames or WolfNames
                #This ensures there will never be more than one instance 
                #with the same name
                globals()['WolfNames'].append(animalName)

                #Actually initializes animal instance
                #i.e. wolf1 = Wolf()

                globals()[animalName] = eval('Wolf'+'(offspringRate=150, health=250)')  

                row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)

                while app.cellColorsList[row][col] == 'blue':

                    row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)


                globals()['WolfPosition'].append([row, col])


    sheepToBeBorn = 0
    sheepThatGaveBirth = 0

    #Declares that new offspring will be born whenever offspringCounter is 
    #equal to that specific animal instance's offspringRate (as each animal 
    #instance could have a different offspringRate due to species and/or mutation)
    for sheep in range(len(SheepNames)):

        offspringCounter = globals()[SheepNames[sheep]].getOffspringCounter()
        offspringRate = globals()[SheepNames[sheep]].getOffspringRate() 

        if offspringCounter < offspringRate:
            globals()[SheepNames[sheep]].addOneToOffspringCounter()
            
        else:
            if sheepThatGaveBirth < len(SheepPosition):
                sheepToBeBorn += 1
            globals()[SheepNames[sheep]].resetOffspringCounter()


        currentSheepHealth = globals()[SheepNames[sheep]].getCurrentHealth()
        currentSheepHungerLevel = globals()[SheepNames[sheep]].getCurrentHungerLevel()
        print("Current Sheep Health:", currentSheepHealth)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
        if currentSheepHungerLevel < 100:
            globals()[SheepNames[sheep]].getHungrier()
        else:
            globals()[SheepNames[sheep]].loseHealth()
            currentSheepHealth = globals()[SheepNames[sheep]].getCurrentHealth()
            print("Current Sheep Health:", currentSheepHealth)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
            print("Current Sheep hunger:", currentSheepHungerLevel)##############################################################SAVE FOR MVP VIDEO TO PROVE THAT IT WORKS
        
        if currentSheepHealth <= 0:
            SheepNames.pop(sheep)
            SheepPosition.pop(sheep)
            break
 


    #Caps combined animal population at 150 to ensure good performance
    if len(WolfPosition) + len(SheepPosition) < 150:    

        #Initializes new sheep offspring
        for _ in range(sheepToBeBorn):

            

            number = random.randrange(1000000000000)
            animalName = '%s%s' % ('Sheep', number)
            if animalName not in globals()['SheepNames']:
                
                #Adds unique name to respective set
                #i.e. SheepNames or WolfNames
                #This ensures there will never be more than one instance 
                #with the same name
                globals()['SheepNames'].append(animalName)

                #Actually initializes animal instance
                #i.e. sheep1 = Sheep()

                globals()[animalName] = eval('Sheep'+'(offspringRate=50, health=100)')  

                row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)

                while app.cellColorsList[row][col] == 'blue':

                    row, col = random.randrange(0, app.rows), random.randrange(0, app.cols)


                globals()['SheepPosition'].append([row, col])
                


#Significantly improves the reliability of the sliders
#Also necessary so that sliders that are on the same y-axis do not move together
def simulateScreen_mouseReleased(app, event): 
    app.ggrSliding = False
    app.aawSliding = False
    app.fgrSliding = False
    app.swpSliding = False
    app.sspSliding = False



def simulateScreen_mousePressed(app, event):

    if app.ggrSliderTopX <= event.x <= app.ggrSliderBottomX and app.ggrSliderTopY <= event.y <= app.ggrSliderBottomY:
        app.ggrSliding = True

    if app.aawSliderTopX <= event.x <= app.aawSliderBottomX and app.aawSliderTopY <= event.y <= app.aawSliderBottomY:
        app.aawSliding = True

    if app.fgrSliderTopX <= event.x <= app.fgrSliderBottomX and app.fgrSliderTopY <= event.y <= app.fgrSliderBottomY:
        app.fgrSliding = True
    
    if app.swpSliderTopX <= event.x <= app.swpSliderBottomX and app.swpSliderTopY <= event.y <= app.swpSliderBottomY:
        app.swpSliding = True

    if app.sspSliderTopX <= event.x <= app.sspSliderBottomX and app.sspSliderTopY <= event.y <= app.sspSliderBottomY:
        app.sspSliding = True

    if app.width/1.885 <= event.x <= app.width/1.315 and app.height/1.1 <= event.y <= app.height - app.margin + 10:
        if app.runSim:
            app.runSim = False

    #The hitbox for the "Start New Simulation" button
    if app.width/1.3 <= event.x <= app.width-app.margin + 10 and app.height/1.1 <= event.y <= app.height - app.margin + 10:

        app.runSim = True
        app.cellColorsList = getCellColorsList(app)
        global animalCount
        animalCount = {'Wolf': wolfCount, 'Sheep': sheepCount}

        for sheep in SheepNames:
            print(globals()[sheep].getOffspringRate())
        for wolf in WolfNames:
            print(globals()[wolf].getOffspringRate())

        initializeAnimals(app)
        


def simulateScreen_mouseDragged(app, event): 

    if app.runSim == False: #prevents changing sliders during a running simulation

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


        #Logic for Average Amount of Water (aaw) slider
        ################################################

        if app.aawSliderTopX <= event.x <= app.aawSliderBottomX and app.aawSliderTopY < event.y < app.aawSliderBottomY:
            app.aawSliding = True

        if app.aawSliding and app.aawLineTopX < event.x < app.aawLineBottomX:
            app.aawSliderTopX = event.x
            app.aawSliderBottomX = app.aawSliderTopX + 8
        elif app.aawSliding and event.x < app.aawLineTopX:
            app.aawSliderTopX = app.aawLineTopX
            app.aawSliderBottomX = app.aawSliderTopX + 8
        elif app.aawSliding and app.aawLineBottomX < event.x:
            app.aawSliderTopX = app.aawLineBottomX
            app.aawSliderBottomX = app.aawSliderTopX + 8

        app.aawNum = int(((app.aawSliderTopX-app.aawLineTopX)/app.aawLineLength)*10)

        #1-10 as the scale is more readable for users, rather than 0-9
        if app.aawNum in [0,1,2,3]: 
            app.aawNum = 1
        elif app.aawNum in [4,5,6]: 
            app.aawNum = 2
        elif app.aawNum in [7,8,9,10]:
            app.aawNum = 3

        #Logic for Flower Growth Rate (fgr) slider
        ################################################
        if app.fgrSliderTopX <= event.x <= app.fgrSliderBottomX and app.fgrSliderTopY < event.y < app.fgrSliderBottomY:
            app.fgrSliding = True

        if app.fgrSliding and app.fgrLineTopX < event.x < app.fgrLineBottomX:
            app.fgrSliderTopX = event.x
            app.fgrSliderBottomX = app.fgrSliderTopX + 8
        elif app.fgrSliding and event.x < app.fgrLineTopX:
            app.fgrSliderTopX = app.fgrLineTopX
            app.fgrSliderBottomX = app.fgrSliderTopX + 8
        elif app.fgrSliding and app.fgrLineBottomX < event.x:
            app.fgrSliderTopX = app.fgrLineBottomX
            app.fgrSliderBottomX = app.fgrSliderTopX + 8

        app.fgrNum = int(((app.fgrSliderTopX-app.fgrLineTopX)/app.fgrLineLength)*10)

        #1-10 as the scale is more readable for users, rather than 0-9
        if app.fgrNum == 0: app.fgrNum = 1
        elif app.fgrNum == 9: app.fgrNum = 10

        #Logic for Starting Wolf Population (swp) slider
        ################################################
        if app.swpSliderTopX <= event.x <= app.swpSliderBottomX and app.swpSliderTopY < event.y < app.swpSliderBottomY:
            app.swpSliding = True

        if app.swpSliding and app.swpLineTopX < event.x < app.swpLineBottomX:
            app.swpSliderTopX = event.x
            app.swpSliderBottomX = app.swpSliderTopX + 8
        elif app.swpSliding and event.x < app.swpLineTopX:
            app.swpSliderTopX = app.swpLineTopX
            app.swpSliderBottomX = app.swpSliderTopX + 8
        elif app.swpSliding and app.swpLineBottomX < event.x:
            app.swpSliderTopX = app.swpLineBottomX
            app.swpSliderBottomX = app.swpSliderTopX + 8

        app.swpNum = int(((app.swpSliderTopX-app.swpLineTopX)/app.swpLineLength)*10)

        #1-10 as the scale is more readable for users, rather than 0-9
        if app.swpNum == 0: app.swpNum = 1
        elif app.swpNum == 9: app.swpNum = 10

        global wolfCount
        wolfCount = app.swpNum

        #Logic for Starting Sheep Population (ssp) slider
        ################################################
        if app.sspSliderTopX <= event.x <= app.sspSliderBottomX and app.sspSliderTopY < event.y < app.sspSliderBottomY:
            app.sspSliding  = True

        if app.sspSliding and app.sspLineTopX < event.x < app.sspLineBottomX:
            app.sspSliderTopX = event.x
            app.sspSliderBottomX = app.sspSliderTopX + 8
        elif app.sspSliding and event.x < app.sspLineTopX:
            app.sspSliderTopX = app.sspLineTopX
            app.sspSliderBottomX = app.sspSliderTopX + 8
        elif app.sspSliding and app.sspLineBottomX < event.x:
            app.sspSliderTopX = app.sspLineBottomX
            app.sspSliderBottomX = app.sspSliderTopX + 8

        app.sspNum = int(((app.sspSliderTopX-app.sspLineTopX)/app.sspLineLength)*10)

        #1-10 as the scale is more readable for users, rather than 0-9
        if app.sspNum == 0: app.sspNum = 1
        elif app.sspNum == 9: app.sspNum = 10

        global sheepCount
        sheepCount = app.sspNum



#Draws the simulation screen
def simulateScreen_redrawAll(app, canvas):

    if app.runSim:

        drawBoard(app, canvas)
        drawWolves(app, canvas)
        drawSheep(app, canvas)
    
    else:
        canvas.create_image(app.width/3.75, app.height/2, image=ImageTk.PhotoImage(app.stockSimWithOverlayWithTextImage))  

    drawGrassGrowthRateSlider(app, canvas)
    drawWaterFallRateSlider(app, canvas)
    drawStartingWolfPopulationSlider(app, canvas)
    drawStartingSheepPopulationSlider(app, canvas)
    drawFlowerGrowthRateSlider(app, canvas)
    drawGraph(app, canvas)

    #Draws "Run Simulation" Button/Text
    canvas.create_rectangle(app.width/1.3, app.height/1.1, app.width - app.margin + 10, app.height - app.margin + 10, fill='black')
    canvas.create_text(app.width/1.133, app.height/1.06, text='Start New Simulation', font='Ariel 30', fill='white')

    #Draws "Pause Simulation" Button/Text
    if app.runSim:
        canvas.create_rectangle(app.width/1.885, app.height/1.1, app.width/1.315, app.height - app.margin + 10, fill='black', outline='black')
    else:
        canvas.create_rectangle(app.width/1.885, app.height/1.1, app.width/1.315, app.height - app.margin + 10, fill='grey', outline='grey')
    canvas.create_text(app.width/1.545, app.height/1.06, text='End Current Simulation', font='Ariel 30', fill='white')

runApp(width=1728, height=905)