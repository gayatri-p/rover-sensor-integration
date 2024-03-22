from time import sleep
import pyfirmata
from StepperLib import Stepper

board = pyfirmata.ArduinoMega('COM19')
reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
reader.start()
print("Communication Successfully started")

dir_pin = 22
step_pin = 23
steps_per_revolution = 200

motor = Stepper(steps_per_revolution, board, dir_pin, step_pin)

while True:
    
    motor.turn_angle(60)
    # motor.switch_direction()
    sleep(0.01)
    motor.turn_angle(-60)
    
    board.exit()
    break