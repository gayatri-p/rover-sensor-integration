""" servo pyfirmata"""

import pyfirmata

class servo:
    def __init__(self,pin):
        self.pin=board.get_pin('d:{}:s'.format(pin))
        
    def move_servo(self,angle):
       self.pin.write(angle)
        


