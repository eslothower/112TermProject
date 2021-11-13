from cmu_112_graphics import *
import random

######################################################################
#Drawing grid
######################################################################

def appStarted(app):
    app.rows = 50
    app.cols = 50
    app.cellSize = 20
    app.margin = 25
    app.colors = ['green', 'tan']

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
            drawCell(app, canvas, row, col)

def drawCell(app, canvas, row, col):
    (x0, y0, x1, y1) = getCellBounds(app, row, col)
    color = random.randint(0,1)
    canvas.create_rectangle(x0, y0, x1, y1, fill=app.colors[color], width = 4)

def redrawAll(app, canvas):
    drawBoard(app, canvas)

def runSim():
    rows = 50
    cols = 50
    cellSize = 20
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


for i in range(4):
    plt.plot(np.random.rand(10))

#plt.show()