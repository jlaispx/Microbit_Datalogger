#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlai
#
# Created:     26/09/2018
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
    name = "datalog.txt"
    with open(name, "r") as f:

        for line in f:
            coords = line.split(',')
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
    ax = fig.gca(projection='3d')

    #
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
