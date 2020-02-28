from NanpyConnect import nanpyConnect
from time import sleep
from MotorClass import Motor

a = nanpyConnect()

M1EnPin = 5 
M1APin = 6
M1BPin = 7
M2EnPin = 8
M2APin = 9
M2BPin = 10
	
# Enable and set each motor
M1 = Motor("LEFT", M1EnPin, M1APin, M1BPin)
M1.pinSet(a)

M2 = Motor("RIGHT", M2EnPin, M2APin, M2BPin)
M2.pinSet(a)