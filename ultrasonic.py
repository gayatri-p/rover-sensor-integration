import pyfirmata
import time

board = pyfirmata.Arduino('COM16')

start = 0
end = 0

echo = board.get_pin('d:11:i')
trig = board.get_pin('d:12:o')
LED = board.get_pin('d:13:o')

it = pyfirmata.util.Iterator(board)
it.start()

trig.write(0)
time.sleep(2)

while True:
    time.sleep(0.5)

    trig.write(1)   
    time.sleep(0.00001)
    trig.write(0)
    
    print(echo.read())
    while echo.read() == False:
        start = time.time()

    while echo.read() == True:
        end = time.time()
    
    TimeElapsed = end - start
    distance = (TimeElapsed * 34300) / 2

    print("Measured Distance = {} cm".format(distance) )
