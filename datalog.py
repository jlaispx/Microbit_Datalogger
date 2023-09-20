
from microbit import *
import os
name = "datalog.txt"
gravity = -992 #default offset gravity
xoff = 0
yoff = 0

def doCalibrate():
    global xoff, yoff, gravity
    iters=100
    x=0
    y=0
    z=0
    for i in range(iters):
        x += accelerometer.get_x()
        y += accelerometer.get_y()
        z += accelerometer.get_z()
        sleep(100)
        if i%10==0:
            display.show(int(i/10))
    xoff = round(x/iters) # calculate average offset
    yoff = round(y/iters)
    gravity = round(z/iters)
    print(xoff, yoff, gravity)

def doLog():
    global xoff, yoff, gravity # pass calibration offsets
    x = accelerometer.get_x()-xoff
    y = accelerometer.get_y()-yoff
    z = accelerometer.get_z()-gravity

    coords = "{},{},{}".format(x, y, z)
    # print(coords)
    return coords

def startLogging():
    #global xoff, yoff, gravity#pass calibration offsets
    try:
        with open(name, "w") as f:
            #f.write("{},{},{}\n".format(xoff,yoff, gravity))
            while True:
                coords = doLog()
                buf = "{}\n".format(coords)
                f.write(buf)
                #print(buf)
                if os.size(name) > 25000:
                    break
                if button_b.is_pressed():
                    display.show(Image.ALL_CLOCKS)
                    break
                sleep(50)
                display.show(Image.HEART)
                sleep(50)
                display.show(Image.PACMAN)
    except OSError:
        print("Can't create file {}".format(name))

# This is main programme
display.clear()
#Loop forever until B pressed
while True:
    if button_a.is_pressed():   # start logging
        display.show(Image.HEART)
        doCalibrate()
        startLogging()
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
        break