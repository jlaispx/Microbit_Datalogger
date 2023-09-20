#-------------------------------------------------------------------------------
# Name:        plotter
# Purpose:     plots a 3D graph representing path of a datalogger using microbit
#
# Author:      jlai
#
# Created:     26/09/2018
# Modified:    21/09/2023 - upgraded matplotlib to version 3.8.0
# Copyright:   (c) jlai 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

test=True
def getDatalog(x,y,z):
    '''
     Input:
                x - empty array to store all x co-ords
                y - empty array to store all y co-ords
                z - empty array to store all z co-ords
                datalog.txt file containing lists of x,y,z co-ords
     Process:
                Read the datalog file and strip each co-ord out and split
                into separate values x,y,z
                Each of the separate co-ords in added to the their
                relevant array. x to x-array, y to y-array etc.
                Return the filled arrays
     Output:
                x - array filled in with all x co-ords
                y - array filled in with all y co-ords
                z - array filled in with all z co-ords
    '''
    name = "datalog2.txt"
    with open(name, "r") as f:
        first=False #True
        for line in f:
            coords = line.strip().split(',')
            print(coords)
            if first:
                first=False
            else:
                x.append(int(coords[0]))
                y.append(int(coords[1]))
                z.append(int(coords[2].strip()))
        print(x,y,z)
    return x,y,z

def drawPath(x,y,z):
    '''
     Input:
                x - array filled in with all x co-ords
                y - array filled in with all y co-ords
                z - array filled in with all z co-ords
     Process:
                Creates the 3D Axes
                Plots using x,y,z co-ords
     Output:
                Shows 3D image
    '''
    fig = plt.figure()
    # Create 3D Axes
    #ax = fig.gca(projection='3d')  # Older version
    ax = fig.add_subplot(projection="3d")  # matplotlib v3.8.0

    # using arrays of x,y,z co-ords, draw flightpath
    ax.plot(x, y, z, label='flight path')
    ax.legend()

    plt.show()

def main():
    x=[]
    y=[]
    z=[]
    x,y,z = getDatalog(x,y,z)
    drawPath(x,y,z)

if __name__ == '__main__':
    main()
