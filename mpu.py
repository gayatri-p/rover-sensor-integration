import time
import board
import adafruit_mpu6050
import threading

class MPU:
    def __init__(self):
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
        self.mpu = adafruit_mpu6050.MPU6050(self.i2c)

    def readmpu(self):
        while True:
            Acceleration=("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (self.mpu.acceleration))
            Gyro=("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (self.mpu.gyro))
            Temperature=("Temperature: %.2f C" % self.mpu.temperature)
            time.sleep(1)

if __name__ == "__main__":
    mpu_instance = MPU()
    
    # Create a thread for reading sensor data
    sensor_thread = threading.Thread(target=mpu_instance.readmpu, daemon=True)
    sensor_thread.start()

    # Main thread can do other tasks or simply wait
    while True:
        time.sleep(1)
