'''
Stepper motor control using the A4988 driver.
Pinout:
1 - ENABLE         16 - V_MOTOR
2 - MICROSTEP 1    15 - GND_MOTOR
3 - MICROSTEP 2    14 - 2B
4 - MICROSTEP 3    13 - 2A
6 - RESET          12 - 1A
6 - SLEEP          11 - 1B
7 - STEP           10 - V_DD
8 - DIRECTION      9  - GND
'''
from time import sleep

class Stepper():
    def __init__(self, board, dir_pin, step_pin, micro_step_pins=(0,0,0), total_steps=200):

        # initializes the pins as outputs
        self.dir_pin = board.get_pin(f'd:{dir_pin}:o')
        self.step_pin = board.get_pin(f'd:{step_pin}:o')
        self.micro_step_pins = [
            board.get_pin(f'd:{micro_step_pins[0]}:o'),
            board.get_pin(f'd:{micro_step_pins[1]}:o'),
            board.get_pin(f'd:{micro_step_pins[2]}:o'),
        ]

        self.step_number = 0 # what number of steps are going to be turned
        self.direction = 0
        self.total_steps = total_steps # total number of steps per revolution
        self.step_delay = 0.001 # time delay between steps

    def set_delay(self, delay):
        self.step_delay = delay

    def switch_direction(self):
        self.direction = 1 if self.direction == 0 else 0
        self.dir_pin.write(self.direction)
    
    def turn_angle(self, angle):
        if angle < 0:
            self.switch_direction()
            angle = -angle

        step_sizes = [360/(200*2**x) for x in range(0,5)] # in degrees

        for i, step_size in enumerate(step_sizes):
            self.set_resolution(i)
            self.step(angle//step_size)

            print(f'1/{2**(i)} steps: {angle//step_size}')
            angle = angle - (angle//step_size)*step_size
            # print('remaining steps', angle/1.8)

        print('remaining angle (error):', angle)

    def step(self, steps):
        for i in range(int(steps)):
            self.step_pin.write(1)
            sleep(self.step_delay)
            self.step_pin.write(0)
            sleep(self.step_delay)

    def set_resolution(self, resolution):
        '''
        Defined resolutions: 1, 1/2, 1/4, 1/8, 1/16 indexed from [0, 4]
        '''
        if resolution == 0: # full step
            states = (0, 0, 0)
        elif resolution == 1: # half step
            states = (1, 0, 0)
        elif resolution == 2: # quarter step
            states = (0, 1, 0)    
        elif resolution == 3: # 1/8th step
            states = (1, 1, 0)
        elif resolution == 4: # 1/16th step
            states = (1, 1, 1)

        for pin, state in zip(self.micro_step_pins, states):
            pin.write(state)

class Stepper_ULN2003():
    def __init__(self, board, pins=(8, 9, 10, 11)):
        self.board = board
        self.pin1, self.pin2, self.pin3, self.pin4 = pins
        self.in1 = board.get_pin(f'd:{self.pin1}:o')
        self.in2 = board.get_pin(f'd:{self.pin2}:o')
        self.in3 = board.get_pin(f'd:{self.pin3}:o')
        self.in4 = board.get_pin(f'd:{self.pin4}:o')
        self.pins = [self.in1, self.in2, self.in3, self.in4]
        self.steps = 4096
        self.step_sleep = 0.000025
        self.step_sequence = [[1,0,0,1],
                              [1,0,0,0],
                              [1,1,0,0],
                              [0,1,0,0],                                                                    
                              [0,1,1,0],
                              [0,0,1,0],
                              [0,0,1,1],
                              [0,0,0,1]]
        
    def rotate(self, num_rotations, direction):
        cnt = 0
        for i in range(num_rotations*self.steps):
            for pin in range(len(self.pins)):
                self.pins[pin].write(self.step_sequence[cnt][pin])
            
            if direction: # clockwise
                cnt = (cnt + 1) % 8
            else: # counter-clockwise
                cnt = (cnt - 1) % 8
            
            sleep(self.step_sleep)