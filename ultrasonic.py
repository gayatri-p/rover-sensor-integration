rom pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM0')  # Change '/dev/ttyACM0' to the port where your Arduino is connected
class ultrasonic:
    def __init__(self,trigger_pin,echo_pin,board):
      trigger_pin=self.trigger_pin
      echo_pin=self.echo_pin
      board=self.board
      trigger = board.get_pin('d:{}:o'.format(trigger_pin))
      echo = board.get_pin('d:{}:i'.format(echo_pin))
      echo.enable_reporting()

    def read_distance():
        # Send a 10us pulse to trigger
        trigger.write(True)
        time.sleep(0.00001)
        trigger.write(False)
        
        # Measure the duration of the echo pulse
        pulse_duration = 0
        while not pulse_duration:
            pulse_duration = echo.read()
    
        # Calculate distance in centimeters
        distance = pulse_duration * 34300 / 2  # Speed of sound is 343 m/s
        return distance

    try:
        while True:
            distance = read_distance()
            print("Distance: %.2f cm" % distance)
            time.sleep(1)
    except KeyboardInterrupt:
        board.exit()
