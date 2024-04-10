""" servo pyfirmata"""

import pyfirmata

class servo:
    def __init__(self,pin,board):
        self.pin=board.get_pin(f'd:{}:s'.{pin})#board will be initialized beforehand
        
    def move_servo(self,angle):
       self.pin.write(angle)
        


