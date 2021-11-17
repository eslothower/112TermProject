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
#Animal Classes
######################################################################

sheep1 = Sheep()
print(sheep1)

######################################################################
#App Started
######################################################################

def appStarted(app):
    #app.mode = "titleScreen"
    app.mode = 'simulateScreen'
    app.rows = 30
    app.cols = 30
    app.cellSize = 25
    app.margin = 25
    app.colors = ['green', 'tan', 'blue']
    app.waterPuddles = random.randrange(3)
    app.waterAmount = 'Regular'
    app.cellColorsList = getCellColorsList(app, app.rows, app.cols)
    app.wolfImage = app.scaleImage(app.loadImage('assets/Modified/black_wolf.png'), 1/10) 
    print(app.cellColorsList)
    print(len(app.cellColorsList))


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

#Creates a list of digits that all correspond to a color. Used for generating the terrain
def getCellColorsList(app, rows, cols):

    resultingList = []
    currentPuddles = 0

    for row in range(rows):
        currentRow = []
        for col in range(cols):
            colorNum = random.randrange(0,3)

            #if blue and still need more puddles
                #Look in all directions
                #If that is a valid position in the grid
                    #Make that postion blue
                    #Look in all positions from there again and repeat
            #else
                #roll again until it's not blue


            # if app.colors[colorNum] == 'blue' and currentPuddles < app.waterPuddles:

            #     currentPuddles += 1

            #     if resultingList[row][col]

            


            currentRow.append(colorNum)
            
        resultingList.append(currentRow)

    return resultingList



def getCellBounds(app, row, col):

    gridWidth  = app.width//2 #this makes the grid go to the left side of the screen
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
    
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black', width = 1)

def simulateScreen_redrawAll(app, canvas):
    canvas.create_rectangle(app.margin, app.margin, (app.width//2) + app.margin, app.height-app.margin, outline='black', width=20)
    drawBoard(app, canvas)
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.wolfImage))  

def runSim():
    # rows = 40
    # cols = 40
    # cellSize = 25
    # margin = 25
    # width = (cellSize * cols) + (2 * margin)
    # height = (cellSize * rows) + (2 * margin)

    #runApp(width=width, height=height)

    runApp(width=1728, height=905)

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