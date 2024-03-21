import pyfirmata
import time

if __name__ == '__main__':
    board = pyfirmata.Arduino('PORT')
    print("Communication Successfully started")
    
    it = pyfirmata.util.Iterator(board)
    it.start()