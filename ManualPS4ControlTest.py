## MANUAL PS4 CONTROLLER TEST

from PygameControllerConnect import psControl
from MotorClass import Motor
from NanpyConnect import nanpyConnect
from Navigation import Navigation
from Trig import Trig
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from math import fabs
import sys

# CONNECT CONTROL AND ARDUINO
ps = psControl()
a = nanpyConnect()

# PIN SETUP
M1En = 5
M1A = 6
M1B = 7
M2En = 8
M2A = 9
M2B = 10

# MOTOR SETUP
M1 = Motor("LEFT", M1En, M1A, M1B)
M2 = Motor("RIGHT", M2En, M2A, M2B)
M1.pinSet(a)
M2.pinSet(a)

print'IF AT ANY POINT THE MOTORS GO WILD, TRY HITTING X'
sleep(3)

while True:
	try:
		sleep(0.005)
		leftJoy = ps.joyStick(1)
		rightJoy = ps.joyStick(4)
		if leftJoy < 0:
			M1.directionSet("S", a)
			M1.pwmSet(leftJoy * -1, a)
			print'Left Joystick: ', leftJoy
		else:
			M1.directionSet("W", a)
			M1.pwmSet(leftJoy, a)

		if rightJoy < 0:
			M2.directionSet("S", a)
			M2.pwmSet(rightJoy * -1, a)
			print'Right Joystick: ', rightJoy
		else:
			M2.directionSet("W",a)
			M2.pwmSet(rightJoy, a)

		print'Left Joystick: ', leftJoy
		print'Right Joystick: ', rightJoy
		xButton = ps.buttonPress(0)
		oButton = ps.buttonPress(1)
		tButton = ps.buttonPress(2)
		sButton = ps.buttonPress(3)
		if xButton == 1:
			M1.stopAll(a)
			M2.stopAll(a)

	except KeyboardInterrupt:
		M1.stopAll(a)
		M2.stopAll(a)
		break
