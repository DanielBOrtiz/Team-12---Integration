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

# Now let's test some movements
try:
	print'Moving FORWARD' # forward turns the motor clockwise
	M1.directionSet("W", a) # Change these values here to change direction of motors
	M2.directionSet("W", a) # Change these values here to change direction of motors
	sleep(1)

	print'Speeding Up'
	for x in range(0, 255):
		M1.pwmSet(x, a)
		M2.pwmSet(x, a)
		print(x)
		sleep(0.0001)

	sleep(0.5)
	print'Slowing Down'
	for x in range(0, 255):
		M1.pwmSet(255-x, a)
		M2.pwmSet(255-x, a)
		print(255-x)
		sleep(0.0001)

	print'Motors Stopped.'
	sleep(0.5)

	print'Moving REVERSE' # forward turns the motor clockwise
	M1.directionSet("S", a) # Change these values here to change direction of motors
	M2.directionSet("S", a) # Change these values here to change direction of motors
	sleep(1)

	print'Speeding Up'
	for x in range(0, 255):
		M1.pwmSet(x, a)
		M2.pwmSet(x, a)
		print(x)
		sleep(0.0001)

	sleep(0.5)
	print'Slowing Down'
	for x in range(0, 255):
		M1.pwmSet(255-x, a)
		M2.pwmSet(255-x, a)
		print(255-x)
		sleep(0.0001)

	print'Motors Stopped.'
	sleep(0.5)

	print'Left Turn'
	M1.directionSet("S", a) # Change these values here to change direction of motors
	M2.directionSet("W", a) # Change these values here to change direction of motors
	sleep(1)

	print'Speeding Up'
	for x in range(0, 255):
		M1.pwmSet(x, a)
		M2.pwmSet(x, a)
		print(x)
		sleep(0.0001)

	sleep(0.5)
	print'Slowing Down'
	for x in range(0, 255):
		M2.pwmSet(255-x, a)
		M1.pwmSet(255-x, a)
		print(255-x)
		sleep(0.0001)



except KeyboardInterrupt:
	M1.stopAll(a)
	M2.stopAll(a)


M1.stopAll(a)
M2.stopAll(a)