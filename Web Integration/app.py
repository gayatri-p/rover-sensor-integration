from flask import Flask, render_template, Response, request
from StepperLib import Stepper 
import pyfirmata2 as pyfirmata

app = Flask(__name__, template_folder='/home/rtc/Desktop/rover-sensor-integration/rover-sensor-integration/templates')


# Default route
@app.route('/', methods =['POST'])
def index():
    # if request.method == "GET":
    base = request.form.get("base-angle")
    hinge1 = request.form.get("hinge1-angle")
    hinge2 = request.form.get("hinge2-angle")
    hinge3 = request.form.get("hinge3-angle")
    print('base:', base)
    print('hinge1:', hinge1)
    print('hinge2:', hinge2)
    print('hinge3:', hinge3)
    return render_template('index.html')

def stepper_controls(board):
    motor_1_configs = (22, 23, (1, 2, 3))
    motor_1 = Stepper(board, *motor_1_configs)

    return

if __name__ == '__main__':

    # board = pyfirmata.Arduino(pyfirmata.Arduino.AUTODETECT)
    # reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
    # reader.start()
    # print("Communication Successfully started")

    app.run(host='0.0.0.0', port=5000, debug=True)
    
    while True:
        stepper_controls(board='')