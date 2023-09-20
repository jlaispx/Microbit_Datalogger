#-------------------------------------------------------------------------------
# Name:        plotter 2
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

dataInterval = 0.2 #seconds

def area(y1,y2,dx):
    return (y1+y2)/2 * dx

def getDistFromAcc1(arrAcc): #lenehan
# convert accelaration array to velocity array
    velocityArray = [0]
    velocity = 0
    for i in range(1,len(arrAcc)):
        velocity += area(arrAcc[i-1]*9.8/1000,arrAcc[i]*9.8/1000,dataInterval)
        velocityArray.append(velocity)

    displacementArray = [0]
    displacement = 0
    for i in range(1,len(velocityArray)):
        displacement += area(velocityArray[i-1],velocityArray[i],dataInterval)
        displacementArray.append(displacement)

    return displacementArray

def getDistFromAcc2(arrAcc):  # Keegan
    t=0.2
    vi=0
    distanceArray=[0]
    d=0
    print("Keegan")
    for a in arrAcc:
        a *=9.8/1000
        d += vi*t + 0.5*a*(t**2)
        vi += a*t
        distanceArray.append(d)
        print(a,vi,d)
    return distanceArray


def getDistFromAcc3(arrAcc): #mine
    t=0.2
    vi=0
    distanceArray=[0]
    d=0
    for a in arrAcc:
        a *=9.8/1000
        vf = vi + a*t
        d += (vi + vf)*t/2
        vi = vf
        distanceArray.append(d)
        #print(a,d)
    return distanceArray

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
    xcurr = 0
    ycurr = 0
    zcurr = 0
    with open(name, "r") as f:
        first=True
        for line in f:
            coords = line.strip().split(',')
            print(coords)
            if first:
                first=False
            else:
                xcurr = (int(coords[0]))
                ycurr = (int(coords[1]))
                zcurr = (int(coords[2].strip()))

                x.append(xcurr)
                y.append(ycurr)
                z.append(zcurr)
        print(f"x[] = {x}")
        print(f"y[] = {y}")
        print(f"z[] = {z}")
    return x,y,z

def drawPath(x,y,z,vLabel):
    '''
     Input:
                x - array filled in with all x co-ords
                y - array filled in with all y co-ords
                z - array filled in with all z co-ords
                vLabel - label the Graph
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
    ax.plot(x, y, z, label=vLabel)
    ax.legend()



def main():
    x=[]
    y=[]
    z=[]
    x,y,z = getDatalog(x,y,z)  #Gets Accelerations
    drawPath(x,y,z,"Acceleration")

    xd=getDistFromAcc1(x)
    yd=getDistFromAcc1(y)
    zd=getDistFromAcc1(z)
    drawPath(xd,yd,zd,"Flight Path (distance) - Lenehan")

    xd=getDistFromAcc2(x)
    yd=getDistFromAcc2(y)
    zd=getDistFromAcc2(z)
    drawPath(xd,yd,zd,"Flight Path (distance) - Aikin")

    xd=getDistFromAcc3(x)
    yd=getDistFromAcc3(y)
    zd=getDistFromAcc3(z)
    drawPath(xd,yd,zd,"Flight Path (distance) - Lai")


    plt.show()
if __name__ == '__main__':
    main()
