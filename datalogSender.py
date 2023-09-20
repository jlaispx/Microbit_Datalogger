from microbit import *
import os
import radio

id = "alpha"
msg1= "startlog"
msg2= "endlog"

def initRadio():
    radio.on
    radio.config(channel=19, power=7)

def radioStart():
    radio.send(msg1)

    # wait for ACK
    for i in range(100):
        incoming=radio.receive()
        if incoming is not None:
            msg = incoming.split(" ")
            if (msg[0] == id) & (msg[1] == "ACK"):
                display.show

def radioStop():
    radio.send(msg2)

initRadio()
display.clear()
while True:
    if button_a.is_pressed():   # start logging
        display.show(Image.HEART)
        doCalibrate()
        display.show(Image.PACMAN)
        startLogging()
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
        break