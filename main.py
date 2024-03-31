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

    steps_to_move = round((30*steps_per_revolution)/360,4)
    print(steps_to_move)
    print('full steps', steps_to_move//1.8)
    steps_to_move = round(steps_to_move%1.8,4)
    print('remaining steps', steps_to_move)
    print()
    
    print('half steps', steps_to_move//0.9)
    steps_to_move = round(steps_to_move%0.9,4)
    print('remaining steps', steps_to_move)
    
    board.exit()
    break
