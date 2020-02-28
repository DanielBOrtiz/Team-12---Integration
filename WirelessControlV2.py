## WIRELESS COMMUNICATION VERSION 2
	# SHOUTOUT TO LUCA GACY

from nanpy import (ArduinoApi, SerialManager)
from NanpyConnect import nanpyConnect
from ManualControl import manualControl
from Navigation import Navigation
from MotorClass import Motor
from Trig import Trig
from math import fabs
from time import sleep
import sys

a = nanpyConnect()

M1En = 6
M1A = 4
M1B = 8
M2En = 11
M2A = 12
M2B = 13

motorK = 2
maxPWM = 255
waypointIteration = 0

M1 = Motor("LEFT", M1En, M1A, M1B)
M2 = Motor("RIGHT", M2En, M2A, M2B)

M1.pinSet(a)
M2.pinSet(a)

# Initiate the classes needed for this file
nav = Navigation()
nav.position() # line that calls the position of the beacon
trig = Trig()

# coordinates of each waypoint in the room, starting from door side clockwise.
xArr = [5.0, 8.0, 5.6, 2.3, 0] # x-coordinates of the waypoints
yArr = [2.9, -1.5, -3.5, 0.3, 0] # y-coorindates of the waypoints
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# the buffer below is the leeway we allow the rover's position to account for
# i.e the position is never 100% accurate so we want a range of values that way once the rover hits those values
# it will perform some action based off these positions
buffer = 0.8
angleBuffer = 45
error = 0
correctionError = 0

# Begin rover movement
M1.directionSet("W", a)
M2.directionSet("W", a)
for x in range(0, 52):
    M1.pwmSet(5*x, a)
    M2.pwmSet(5*x, a)
    sleep(0.01)
AUTO = True
MANUAL = True

while AUTO:
	try:
		try:
			sleep(0.5)
			nav.position()
			x1 = x2
			y1 = y2
			x2 = nav.position()[1]
			y2 = nav.position()[2]
			#print'X: ', x2 
			#print'Y: ', y2
	    			#print(xArr[waypointIteration])
				#print(yArr[waypointIteration])

			# The points below are the conditions for the rover to know to set its current position as its new home
			# and to set the next waypoint's x and y-coordinates to xFinal and yFinal
			# since it will be starting by the door the next waypoint will be the tape by the machine shop door
			# xFinal and yFinal will be updated to the next waypoint when the rover reaches the first waypoint
			xFinal = xArr[waypointIteration]
			yFinal = yArr[waypointIteration]
		
			# Find the angle between the x-axis and the vector created by rover's velocity
			velocityTheta = trig.theta(x1, y1, x2, y2)

			# Find the angle between the x-axis and the waypoint vector
			waypointTheta = trig.theta(x2, y2, xFinal, yFinal)

			# Find the difference between the desination theta and velocity theta
			error = waypointTheta - velocityTheta
			if (abs(error) < angleBuffer):
				correctionError = waypointTheta - velocityTheta
				print'Correction Error:', correctionError
					
			#if (abs(error) < angleBuffer):
			#	print'angleBuffer - abs(error)', angleBuffer-abs(error)
			#	sleep(1)
			#	error = waypointTheta - velocityTheta
			#	sleep(1)
			#	print'Error', error
			else:
				print'Error larger than buffer, ignoring error.'
	
			if (xFinal-buffer <= nav.position()[1] <= xFinal+buffer):
				if (yFinal-buffer <= nav.position()[2] <= yFinal+buffer):
					error = 0
					print'Stop!'
					for x in range(0, 52):
						M1.pwmSet(255-5*x, a)
						M2.pwmSet(255-5*x, a)
						print(255-5*x)
						sleep(0.00001)
					print'Current X:', nav.position()[1], 'Current Y:', nav.position()[2]
					print'xFinal:', xFinal, 'yFinal:', yFinal
					print'WAYPOINT:', x+1, 'REACHED'
					sleep(0.5)
					print'Turning Right'
					for x in range(0, 52):
						M1.pwmSet(5*x, a)
						print'Motor 1 PWM:', 5*x
						sleep(0.01)
						waypointIteration += 1
					if (waypointIteration == 4):
						print'Final waypoint reached. We done.'
						M1.stopAll(a)
						M2.stopAll(a)
						next = raw_input('Continue? [y/n]:')
						if (next == 'y'):
							waypointIteration = 0
							M1.stopAll(a)
							M2.stopAll(a)
							#sys.exit()
							AUTO = True
							break
						elif (next == 'n'):
							print'Exiting program...'
							print'If program fails to exit enter CTRL+Z.'
							M1.stopAll(a)
							M2.stopAll(a)
							sys.exit()
							AUTO = False
							break
						else:
							print'Invalid input entered. Exiting program...'
							print'If program fails to exit enter CTRL+Z.'
							M1.stopAll(a)
							M2.stopAll(a)
							AUTO = False
							break

					sleep(2)
					print'Proceed.'
					M1.directionSet("W", a)
					M2.directionSet("W", a)
					for x in range(0, 52):
						M1.pwmSet(5*x, a)
						M2.pwmSet(5*x, a)
						sleep(0.0001)
					sleep(2)
					break

			if (correctionError > 0):
				print'Correct Right!' # Got rid of exclamation points cuz Mackenzie rude af
				print'ERROR for Right turn:', correctionError
				rightSlow = 255 - correctionError * motorK
				print'Decreasing Right Motor:', rightSlow
				M1.pwmSet(rightSlow, a)
				M2.pwmSet(maxPWM, a)		
	
			if (correctionError < 0):
				print'Correct Left!' 
				print'ERROR for Left turn:', correctionError
				leftSlow = 255 + correctionError * motorK # sign here is positive because the angle is negative
				print'Decreasing Left Motor:', leftSlow
				M1.pwmSet(maxPWM, a)
				M2.pwmSet(leftSlow, a)
	
		except KeyboardInterrupt:
			M1.stopAll(a)
			M2.stopAll(a)
			manualControl(a, M1, M2, MANUAL) # This sends the code into Manual Control
			AUTO = manualControl(a, M1, M2, MANUAL)		# For more info refer to ManualControl.py
			print'HERE'
	
	except KeyboardInterrupt:
		M1.stopAll(a)
		M2.stopAll(a)
