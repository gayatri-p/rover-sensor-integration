""" servo pyfirmata"""
from time import sleep

class Servo:
    def __init__(self, board, pin):
        self.pin = pin
        self.servo = board.get_pin(f'd:{pin}:s')
        self.steps = 30
        self.delay = 25/(1000*self.steps)
        
    def turn_angle(self, angle):
        start = self.servo.read()
        if start < angle:
            for i in range(self.steps*start, self.steps*angle+1):
                self.servo.write(i/self.steps)
                sleep(self.delay)
        else:
            for i in range(self.steps*start, self.steps*angle-1, -1):
                self.servo.write(i/self.steps)
                sleep(self.delay)
        


