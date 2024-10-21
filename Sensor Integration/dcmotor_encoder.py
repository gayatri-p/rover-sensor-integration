import time
import threading
from pyfirmata2 import Arduino, util

# Define pin numbers
ENCA = 2  # Encoder pin A (YELLOW)
ENCB = 3  # Encoder pin B (WHITE)
PWM = 5  # PWM pin for motor speed control
IN1 = 6
IN2 = 7

# Initialize Arduino board
board = Arduino('/dev/ttyACM0')  # Change '/dev/ttyUSB0' to the port where your Arduino is connected

# Set the pins
encoder_pin_A = board.get_pin('d:{}:i'.format(ENCA))
encoder_pin_B = board.get_pin('d:{}:i'.format(ENCB))

# Set up motor control pins
motor_pwm = board.get_pin('d:{}:p'.format(PWM))
motor_in1 = board.get_pin('d:{}:o'.format(IN1))
motor_in2 = board.get_pin('d:{}:o'.format(IN2))

# Initialize position variable
position = 0

# Previous state of pin A
prev_A_state = 0

# Function to read encoder
def read_encoder():
    global position, prev_A_state
    while True:
        A_state = encoder_pin_A.read()
        if A_state != prev_A_state:
            B_state = encoder_pin_B.read()
            if B_state:
                position += 1
            else:
                position -= 1
            prev_A_state = A_state
        # print(position)

# Start the encoder reading thread
encoder_thread = threading.Thread(target=read_encoder)
encoder_thread.daemon = True  # Daemonize the thread so it will be terminated when the main program exits
encoder_thread.start()

# Function to control the motor
def control_motor(speed, direction):
    motor_pwm.write(speed)
    if direction ==0:
        motor_in1.write(1)
        motor_in2.write(0)
    else :
        motor_in1.write(0)
        motor_in2.write(1)

# Main loop for manual motor control
if __name__ == "__main__":
    try:
        while True:
            speed = float(input("Enter motor speed (0-1): "))
            direction = int(input("Enter motor direction (0 for counter-clockwise, 1 for clockwise): "))
            control_motor(speed, direction)

    except KeyboardInterrupt:
        # Clean up when the program is interrupted
        motor_pwm.write(0)  # Stop the motor
        board.exit()  # Exit the board
