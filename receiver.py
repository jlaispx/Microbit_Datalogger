##
## The Receiver's job is to:
## 1. Notify the Sender to Start/Stop
## 2. Receive Messages from the Sending Microbit.
## NOTE:  Change the Channel number in the Sender and Receiver
##        to prevent overlap from another Microbit
##
from microbit import *
import radio
radio.on()
radio.config(channel=19, power=7)
## File stored on Microbit for future download
filename = "datalog.txt"

def receiveData(f):
    message = radio.receive()
    print(message)
    msg=str(message).split(",")
    print(msg)
    f.write("{}\n".format(msg))
    #x=msg[0]
    #y=msg[1]
    #z=msg[2]
    #print(x,y,z)
    
with open(filename,"w") as f:
    start=False
    while True:
        if button_a.was_pressed():
            radio.send("start")
            display.show(Image.SMILE)
            start=True
        if button_b.was_pressed():
            radio.send("stop")
            display.show(Image.SAD)
            start=False
        if start:
            receiveData(f)

        sleep(200)