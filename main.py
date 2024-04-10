from time import sleep
import numpy as np
import pyfirmata2 as pyfirmata
from StepperLib import Stepper

board = pyfirmata.Arduino(pyfirmata.Arduino.AUTODETECT)
reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
reader.start()
print("Communication Successfully started")

dir_pin = 2
step_pin = 3
steps_per_revolution = 200

motor = Stepper(steps_per_revolution, board, dir_pin, step_pin, micro_step_pins=(8, 9, 10))

while True:
    
    motor.turn_angle(120)
    sleep(1)
    motor.switch_direction()
    motor.turn_angle(60)

    ''' test resolutions '''
    # motor.set_resolution(0)
    # motor.step(200)
    # sleep(2)
    # motor.set_resolution(1)
    # motor.step(400)
    # sleep(2)
    # motor.set_resolution(2)
    # motor.step(800)
    # sleep(2)
    # motor.set_resolution(3)
    # motor.step(1600)
    # sleep(2)
    # motor.set_resolution(4)
    # motor.step(3200)
    
    board.exit()
    break
