from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from MotorClass import Motor
try:
	connection = SerialManager(device='/dev/ttyUSB0') # must manually set port
	a = ArduinoApi(connection = connection)
	print'Connection to Arduino was successful!'
	sleep(0.25)
except:
	print'Failed to Connect to Arduino. :('

M1EnPin = 6 
M1APin = 7
M1BPin = 8
M2EnPin = 11
M2APin = 12
M2BPin = 13

# Enable and set each motor
M1 = Motor("LEFT", M1EnPin, M1APin, M1BPin)
M1.pinSet(a)

M2 = Motor("RIGHT", M2EnPin, M2APin, M2BPin)
M2.pinSet(a)

M1.directionSet("W", a) # Change these values here to change direction of motors
M2.directionSet("W", a)
sleep(1)

print'Right Turn'
for x in range(0, 52):
 	M1.pwmSet(5*x, a)
	print'Motor 1 PWM:', 5*x
	sleep(0.01)

sleep(2)

print'Going forward'
M1.directionSet("W", a)
M2.directionSet("W", a)
for x in range(0, 255):
    M1.pwmSet(x, a)
    M2.pwmSet(x, a)
    sleep(0.01)

M1.stopAll(a)
M2.stopAll(a)