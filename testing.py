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