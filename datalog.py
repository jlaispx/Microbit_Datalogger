from microbit import *
import os
name = "datalog.txt"
g = 992
def doLog():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()+g

    coords = "{},{},{}  ".format(x, y, z)
    # print(coords)
    return coords

def startLogging():
    try:
        with open(name, "w") as f:
            while True:
                coords = doLog()
                buf = "{}\n".format(coords)    
                f.write(buf)
                print(buf)
                if os.size(name) > 25000:
                    break
                if button_b.is_pressed():
                    display.show(Image.ALL_CLOCKS)
                    break
                sleep(250)
                display.show(Image.HEART)
                sleep(250)
                display.show(Image.PACMAN)
    except OSError:
        print("Can't create file %s" % name)

display.clear()
while True:
    if button_a.is_pressed():   # start logging
        display.show(Image.HEART)
        startLogging()
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
        break