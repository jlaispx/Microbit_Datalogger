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

name = "datalog.txt"
with open(name, "r") as f:
    x=[]
    y=[]
    z=[]

    for line in f:
        coords = line.split(',')
        x.append(int(coords[0]))
        y.append(int(coords[1]))
        z.append(int(coords[2].strip()))
    print(x,y,z)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(x, y, z, label='flight path')
    ax.legend()

    plt.show()