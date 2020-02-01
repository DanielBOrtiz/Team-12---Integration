import RPi.GPIO as IO 
from time import sleep

# Set board to read pins by pin number not GPIO number
IO.setmode(IO.BOARD)
IO.setwarnings(False)

# Set motor and PWM pins 
M1A = 11
M1B = 13
M1En = 12 # PWM pin

M2A = 22
M2B = 24
M2En = 23 # PWM pin

# Set sevro signal pin
servoSig = 33

# Setting these  pins as output pins on the Pi
IO.setup(M1A, IO.OUT)
IO.setup(M1B, IO.OUT)
IO.setup(M1En, IO.OUT)
IO.setup(M2A, IO.OUT)
IO.setup(M2B, IO.OUT)
IO.setup(M2En, IO.OUT)
IO.setup(servoSig, IO.OUT)

# Set PWM pins to output PWM w/ 200 Hz frequency
pwm1 = IO.PWM(M1En, 200)
pwm2 = IO.PWM(M2En, 200)
servo = IO.PWM(servoSig, 150)

# Servo config is 6.0, far clock, 17.5 straight, 30 far counterclock

def m1Drxn(drxn):
	if drxn == 'w' or drxn == 'W':
		IO.output(M1A, IO.HIGH)
		IO.output(M1B, IO.LOW)

	if drxn == 's' or drxn == 'S':
		IO.output(M1A, IO.LOW)
		IO.output(M1B, IO.HIGH)

def m2Drxn(drxn):
	if drxn == 'w' or drxn == 'S':
		IO.output(M2A, IO.HIGH)
		IO.output(M2B, IO.LOW)
	if drxn == 's' or drxn == 's':
		IO.output(M2A, IO.LOW)
		IO.output(M2B, IO.HIGH)

def speedChange(speed):
	if speed == 'l' or speed == 'L':
		for x in range (0, 25, 2):
			pwm1.ChangeDutyCycle(x)
			pwm2.ChangeDutyCycle(x)
			sleep(0.08)
	if speed == 'm' or speed == 'M':
		for x in range(25, 50, 2):
			pwm1.ChangeDutyCycle(x)
			pwm2.ChangeDutyCycle(x)
			sleep(0.08)
	if speed == 'h' or speed == 'H':
		for x in range(50, 80, 10):
			pwm1.ChangeDutyCycle(x)
			pwm2.ChangeDutyCycle(x)
			sleep(0.333)

def servoTurn(drxn):
	if drxn == 'a' or drxn == 'A':
		print("Turning Left")
		for x in range (17, 30, 2):
			servo.ChangeDutyCycle(30)
			sleep(0.15)
	if drxn == 'd' or drxn == 'D':
		print("Turning Right")
		for x in range(6, 17, 2):
			servo.ChangeDutyCycle(23-x)
			sleep(0.15)
	if drxn == 'w' or drxn == 'W':
		print("Straightening Servo")
		servo.ChangeDutyCycle(17.5)

pwm1.start(0)
pwm2.start(0)
servo.start(17.5)

while True: 
	userIn = raw_input()
	if userIn == 'l' or userIn == 'L':
		speedChange(userIn)
		continue
	if userIn == 'm' or userIn == 'M':
		speedChange(userIn)
		continue
	if userIn == 'h' or userIn == 'H':
		speedChange(userIn)
		continue

	if userIn == 'w' or userIn == 'W':
		m1Drxn(userIn)
		m2Drxn(userIn)
		print("Forward")
		servoTurn(userIn)
		continue	
	elif userIn == 's' or userIn == 's':
		m1Drxn(userIn)
		m2Drxn(userIn)
		print("Reverse")
		continue

	elif userIn == 'a' or userIn == 'A':
#		if m1direction(userIn) == 'w' or m1direction(userIn) == 'W':
		m1Drxn('w')
		m2Drxn('s')
		pwm1.ChangeDutyCycle(75) 
		pwm2.ChangeDutyCycle(20)
		servoTurn(userIn)
		continue	
	elif userIn == 'd' or userIn == 'D':
#		if m1direction(userIn) == 'w' or m1direction(userIn) == 'W':
		m1Drxn('s')
		m2Drxn('w')
		pwm1.ChangeDutyCycle(20)
		pwm2.ChangeDutyCycle(75)
		servoTurn(userIn)
		continue

	if userIn == 'q' or userIn == 'Q':
		break

IO.cleanup()
