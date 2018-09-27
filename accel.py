from microbit import *
import math
import os
name = "datalog.txt"

def doLog():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    a = accelerometer.get_values()

    coords = "{},{},{}\n".format(x, y, z)
    coords = f"{x},{y},{z}\n"
    # print(coords)
    acceleration = math.sqrt(x**2 + y**2 + z**2)
    # print("acceleration (milli-gs)", acceleration)
    return (coords, acceleration)

def startLogging():
    try:
        with open(name, "w") as f:
            while True:
                (coords, acceleration) = doLog()
                buf = "{}".format(coords)     # "{}:{}".format(coords, acceleration)
                f.write(buf)
                print(buf)
                # print(micropython.mem_info())
                # waprint(os.size(name))
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


