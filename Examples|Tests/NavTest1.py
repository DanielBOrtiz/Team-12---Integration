from Position import currentpos
from Ultrasonic import Ultrasonic
from Navigation import Navigation
from Servo import Servo
from trig import Trig
from math import fabs
import RPi.GPIO as IO
import sys
from time import sleep

# Ask user to enter current beacon address
addr = input("Who is we?")
# Initiate the classes needed for this file
nav = Navigation(addr)
nav.position()
trig = Trig()

# coordinates of each waypoint in the room, starting from door side clockwise.
xArr = [5.3, 8.5, 5.6, 2.3, 0] # x-coordinates of the waypoints
yArr = [2.9, -1.4, -3.8, 0.3, 0] # y-coorindates of the waypoints
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# the buffer below is the leeway we allow the rover's position to account for
# i.e the position is never 100% accurate so we want a range of values that way once the rover hits those values
# it will perform some action based off these positions
buffer = 0.5
angleBuffer = 45

while True:
	for x in range(0, 5):
		if x == 4:
			print("Final waypoint reached. We done.")
			sys.exit()
			break
#			x = 0; # if x becomes larger than our array size, restart this loop so it can go in circles around room
		else:
			while True:
				# Rover will start, move a lil then start saving points as x1 and y1
				sleep(0.5)
# test lines			print(xArr[x])
# test lines			print(yArr[x])
	
				nav.position()
				x1 = x2
				y1 = y2
				x2 = nav.position()[1]
				y2 = nav.position()[2]
				print'X: ', x2 
				print'Y: ', y2

				# The points below are the conditions for the rover to know to set its current position as its new home
				# and to set the next waypoint's x and y-coordinates to xFinal and yFinal
				# since it will be starting by the door the next waypoint will be the tape by the machine shop door
				# xFinal and yFinal will be updated to the next waypoint when the rover reaches the first waypoint
				xFinal = xArr[x]
				yFinal = yArr[x]
#				print(xArr[x])
#				print(yArr[x])

				# find the angle between the x-axis and the vector created from the starting point to where the rover currently is
				velocityTheta = trig.theta(x1, y1, x2, y2) # find angle between axis and current velocity vector

				# find the angle between the x-axis and the vector that points to the the destination waypoint
				waypointTheta = trig.theta(x2, y2, xFinal, yFinal) # find angle between axis and waypoint vector

				# find the difference between the second angle and the first, this will let the rover know how many degrees to correct
				error = waypointTheta - velocityTheta
					
				if abs(waypointTheta - velocityTheta) < angleBuffer:
					error = waypointTheta - velocityTheta


				if xFinal-buffer <= nav.position()[1] <= xFinal+buffer:
					if yFinal-buffer <= nav.position()[2] <= yFinal+buffer:
						error = 0
						print'Stop!'
						print'Turn Right!'
						print'Current X: ', nav.position()[1] 
						print'Current Y: ', nav.position()[2]
						print'DESTINATION:', x+1
						print'xFinal:', xFinal
						print'yFinal:', yFinal
						print'WAYPOINT', x+1, 'REACHED'
#						servo.turn(10)
						x += 1
						sleep(2)
						break

				elif error > 0: # due to inaccuracy of the beacon we choose to ignore differences in angles above 15 degrees, + and -
# Test Line				print'XFINAL - BUFFER =', xFinal-buffer
# Test Line				print'YFINAL - BUFFER =', yFinal-buffer
# Test Line				print'XFINAL + BUFFER =', xFinal+buffer
# Test Line 				print'YFINAL + BUFFER =', yFinal+buffer
# Test Line				print'THIS IS XFINAL:', xFinal
# Test Line 				print'THIS IS YFINAL:', yFinal
# Test Line				print'X: ', nav.position()[1] 
# Test Line				print'Y: ', nav.position()[2]
					print'Correct Right!!'
					print'ERROR for Right Turn:', error
#					sleep(0.4)

				elif error < 0:
#					print'X: ', nav.position()[1] 
#					print'Y: ', nav.position()[2]
					print'Correct Left!!'
					print'ERROR for Left Turn:', error
#					sleep(0.4)
		




