## Sender - stored inside Rocket
## When RESET pressed will:
## 1. Sleep until receive a "Start" from Receiver
##    a. Gets x,y,z acceleration from accelerometer
##    b. Formats it as comma separated list
##    c. Uses Radio to broadcast this data
## 2. Receives Message from Receiving Microbit to Start/Stop
## NOTE: Change the Channel to a unique number with Receiver to prevent overlap
##
from microbit import *
import radio
radio.on()
radio.config(channel=19, power=7)

def sendData():
    x=accelerometer.get_x()
    y=accelerometer.get_y()
    z=accelerometer.get_z()
    coords="{},{},{}".format(x,y,z)
    radio.send(coords)
    display.show(Image.HEART_SMALL)
    sleep(100)
    display.show(Image.HEART)

start = False
while True:
    sleep(20)
    if start:
        sendData()
        
    message = radio.receive()
    if message=="start":
        start=True
        display.show(Image.SMILE)
    elif message=="stop":
        start=False
        display.show(Image.SAD)
        