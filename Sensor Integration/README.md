# Contents

Use pyfirmata2 with Arduino wherever necessary.

- Inverse Kinematics (with [one hinge](Sensor%20Integration/inverse%20kinematics/inverse_kin%202%20arms.py) and [two hinges](Sensor%20Integration/inverse%20kinematics/inverse_kin%203%20arms.py))
- [Working arm controller](Sensor%20Integration/arm_working.ipynb) (rotates the arm to a given $(x,y,z)$ coordinate)
- [Manipulator Base Alignment](Sensor%20Integration/basealign.py) (rotates the arm base to a given angle)
- Arduino Integrations
  - [Servo Motor](Sensor%20Integration/servo/servo.py)
  - [Ultrasonic Sensor](Sensor%20Integration/ultrasonic/ultrasonic.py)
  - Stepper Motor ([A4988 driver](Sensor%20Integration/StepperLib.py))
  - [DC Motor](Sensor%20Integration/dcmotor_encoder.py)
  - [MPU 6050](Sensor%20Integration/mpu6050.py) (accelerometer and gyroscope module)
  - [NRF 2401](Sensor%20Integration/nrf.py) (wireless transceiver)
