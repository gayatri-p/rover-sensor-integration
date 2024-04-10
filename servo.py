""" servo pyfirmata"""

import pyfirmata

class servo:
    def __init__(self,pin):
        self.pin=board.get_pin(f'd:{}:s'.{pin})
        
    def move_servo(self,angle):
       self.pin.write(angle)
        


