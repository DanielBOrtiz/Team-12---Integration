## First iteration of Autonomous Navigation of Rover
	# Shoutout to Luca Gacy 

from nanpy import (ArduinoApi, SerialManager)
from Navigation import Navigation
from MotorClass import Motor
from Trig import Trig
from math import fabs
import sys
from time import sleep


try:
	connection = SerialManager(device='/dev/ttyUSB3') # must manually set port
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

motorK = 3 # influence factor to influence motor PWM
maxPWM = 255
	
# Enable and set each motor
M1 = Motor("LEFT", M1EnPin, M1APin, M1BPin)
M2 = Motor("RIGHT", M2EnPin, M2APin, M2BPin)

M1.pinSet(a)
M2.pinSet(a)

# Ask user to enter current beacon address
addr = input("Who is we?")
# Initiate the classes needed for this file
#nav = Navigation(addr)
#nav.position()
#trig = Trig()

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

# Begin rover movement
M1.directionSet("W", a)
M2.directionSet("W", a)
print'Here'
for x in range(0, 255):
    	M1.pwmSet(x, a)
    	M2.pwmSet(x, a)
	print(x)
   	sleep(0.01)
sleep(2)
nav.position()

M1.stopAll(a)
M2.stopAll(a)