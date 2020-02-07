from Position import currentpos
from Ultrasonic import Ultrasonic
from trig import Trig
import sys
from time import sleep

addr = input("Who is we?")
myPos = currentpos(addr)
#uSensor = Ultrasonic(11, 13) #uncomment this line to measure distance with the ultrasonic sensor along with the print line below
trig = Trig()

# coordinates of each waypoint in the room, starting from door side clockwise.
xArr = [5.6, 8.5, 5.6, 1.8] # x-coordinates of the waypoints
yArr = [3.2, -1.5, -4.4, -0.4] # y-coorindates of the waypoints
w4xFinal = xArr[0] # the final waypoint is just equal to the first point
w4yFinal = yArr[0]

# the buffer below is the leeway we allow the rover's position to account for
# i.e the position is never 100% accurate so we want a range of values that way once the rover hits those values
# it will perform some action based off these positions
buffer = 0.8

while True:

	for x in range(0, 4):
		if x == 5:
			x = 0; # if x becomes larger than our array size, restart this loop so it can go in circles around room
		else:
# test lines		print(xArr[x])
# test lines		print(yArr[x])
	
			# Rover will start, move a lil then start saving points as x1 and y1
			sleep(0.25)
			myPos.position()
			x1 = myPos.position()[1]
			y1 = myPos.position()[2]
#			print'X: ', myPos.position()[1] 
#			print'Y: ', myPos.position()[2]
#			print'Obstacle Distance:',uSensor.ping(), 'cm' # uncomment this line if you wanna print distance measured by sensor

			# program will wait a sec, then set the current position as x2 and y2
			sleep(0.25)
			x2 = myPos.position()[1]
			y2 = myPos.position()[2]
			# find the angle between the x-axis and the vector created from the starting point to where the rover currently is
			theta1 = trig.theta(x1, y1, x2, y2)
#			print'Theta 1:',theta1 # uncomment if you wanna print that angle
			# set the old x1 and y1 equal to current position
			x1 = x2
			y1 = y2


			# The points below are the conditions for the rover to know to set its current position as its new home
			# and to set the next waypoint's x and y-coordinates to xFinal and yFinal
			# since it will be starting by the door the next waypoint will be the tape by the machine shop door
			# xFinal and yFinal will be updated to the next waypoint when the rover reaches the first waypoint
			xFinal = xArr[x]
			yFinal = yArr[x]
			print(xArr[x])
			print(yArr[x])

			# find the angle between the x-axis and the vector that points to the the destination waypoint
			theta2 = trig.theta(x1, y1, xFinal, yFinal)
#			print'Theta 2:', theta2 # uncomment if you wanna print that angle
			# find the difference between the second angle and the first, this will let the rover know how many degrees to correct
			error = theta2 - theta1
#			mag = trig.magntiude()
#			print'ERROR:', error
	
			if -25 <= error < 0: # due to inaccuracy of the beacon we choose to ignore differences in angles above 40 degrees, + and -
				if myPos.position()[1] != xFinal-buffer and myPos.position()[2] != yFinal-buffer:
					if myPos.position()[1] != xFinal+buffer and myPos.position()[2] != yFinal+buffer:
#						print'XFINAL - BUFFER =', xFinal-buffer
#						print'YFINAL - BUFFER =', yFinal-buffer
#						print'XFINAL + BUFFER =', xFinal+buffer
#						print'YFINAL + BUFFER =', yFinal+buffer
#						print'THIS IS XFINAL:', xFinal
#						print'THIS IS YFINAL:', yFinal
#						print'X: ', myPos.position()[1] 
#						print'Y: ', myPos.position()[2]
						print'YEET Right!!'
						print'ERROR for Right Turn:', error
						sleep(0.25)

			if 0 < error <= 25:
				if myPos.position()[1] != xFinal-buffer and myPos.position()[2] != yFinal-buffer:
					if myPos.position()[1] != xFinal+buffer and myPos.position()[2] != yFinal+buffer:
#						print'X: ', myPos.position()[1] 
#						print'Y: ', myPos.position()[2]
						print'YEET Left!!', error
						print'ERROR for Left Turn:', error
						sleep(0.25)

			if xFinal-buffer <= myPos.position()[1] <= xFinal+buffer:
				if yFinal-buffer <= myPos.position()[2] <= yFinal+buffer:
					print'Stop!'
					print'Turn Right!'
					print'Current X: ', myPos.position()[1] 
					print'Current Y: ', myPos.position()[2]
					print'DESTINATION:', x+1
					print'yFinal:', yFinal
					print'yFinal:', yFinal
					print'WAYPOINT', x, 'REACHED'
					x += 1
					sleep(2)
	
			else:
				print'Proceed.'
			
#			break
#			print'THIS IS X:', x
#			x += 1 # increment x
