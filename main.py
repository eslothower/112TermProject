from cmu_112_graphics import *
import random


######################################################################
#Animal Classes
######################################################################

class Animal(object):

    def __init__(self):
        self.offspringRate = 0
        self.hunger = 0
        self.hungerLevel = 0
        self.thirst = 0
        self.thirstLevel = 0
        self.lifespan = 0
        self.age = 0
        self.mutationRate = 0
        self.mutationStatus = False 
        self.nutritionalValue = 0
        self.speed = 0

    def __repr__(self):
        return("I am an animal object")


class Sheep(Animal):

    def __init__(self):
        return

class Wolf(Animal):

    def __init__(self):

        self.offspringRate = 10 #wolf/cycle
        #self.hunger = 
        
        if random.randrange(0,11) == random.randrange(0,11):

            self.mutationStatus = True

        

sheep1 = Sheep()
print(sheep1)


######################################################################
#Drawing grid
######################################################################

def appStarted(app):
    app.rows = 40
    app.cols = 40
    app.cellSize = 25
    app.margin = 25
    app.colors = ['green', 'tan', 'blue']
    app.waterPuddles = 2
    app.waterAmount = 'Regular'
    app.cellColorsList = getCellColorsList(app, app.rows, app.cols)
    
    #app.cellColors = [[random.randrange(0,2) for _ in range(app.rows)] for _ in range(app.cols)]
    print(app.cellColorsList)
    print(len(app.cellColorsList))


#Creates a list of digits that all correspond to a color. Used for generating the terrain
def getCellColorsList(app, rows, cols):

    resultingList = []
    currentPuddles = 0

    for row in range(rows):
        currentRow = []
        for col in range(cols):
            colorNum = random.randrange(0,3)


            # if app.colors[colorNum] == 'blue' and currentPuddles < app.waterPuddles:

            #     currentPuddles += 1

            #     if resultingList[row][col]

            


            currentRow.append(colorNum)
            
        resultingList.append(currentRow)

    return resultingList



def getCellBounds(app, row, col):

    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def drawBoard(app, canvas):   
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.cellColorsList[row][col]
            drawCell(app, canvas, row, col, app.colors[color])

def drawCell(app, canvas, row, col, color):
    (x0, y0, x1, y1) = getCellBounds(app, row, col)
    
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, width = 4)

def redrawAll(app, canvas):
    drawBoard(app, canvas)

def runSim():
    rows = 40
    cols = 40
    cellSize = 25
    margin = 25
    width = (cellSize * cols) + (2 * margin)
    height = (cellSize * rows) + (2 * margin)

    runApp(width=width, height=height)

runSim()


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