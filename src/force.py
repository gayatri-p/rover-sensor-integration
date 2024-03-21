import pyfirmata

def read_force(board, pin):
    sensor = board.analog[pin]
    sensor.enable_reporting()
    
    force = sensor.read()
    return force