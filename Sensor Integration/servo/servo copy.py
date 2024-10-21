from pyfirmata import Arduino, SERVO
from time import sleep

port=''
pin=10
board=Arduino(port)

board.digital[pin].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

while True:
    for i in range(0,100):
        rotateServo(pin,i)
    for i in range(180,1,-1):
        rotateServo(pin,i)
    