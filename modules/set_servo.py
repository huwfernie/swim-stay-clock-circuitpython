# https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo
# https://learn.adafruit.com/using-servos-with-circuitpython/high-level-servo-control
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
servo = servo.Servo(pwm, min_pulse=750, max_pulse=2250)

def set(name):
    print("set servo to '", name, "'")
    if name == "ERROR":
        servo.angle = 0
    if name == "WORKING":
        servo.angle = 30
    if name == "SWIM":
        servo.angle = 60
    if name == "SEWAGE":
        servo.angle = 90