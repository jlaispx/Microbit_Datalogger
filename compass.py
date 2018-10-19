from microbit import *
compass.calibrate()
while True:
    display.clear()
    bearing = compass.heading()
    print(bearing)
    sleep(100)