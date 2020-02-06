from Position import currentpos
from Ultrasonic import Ultrasonic
from trig import Trig
import sys
from time import sleep

addr = input("Who is we?")
myPos = currentpos(addr)
uSensor = Ultrasonic(11, 13)
trig = Trig()

x1 = 1.8
y1 = -0.4
x1 = 0
x2 = 0
xFinal = 5.2
yFinal = 3

while True:
	sleep(1)
	myPos.position()
	print'X: ', myPos.position()[1] 
	print'Y: ', myPos.position()[2]
	print'Distance:',uSensor.ping(), 'cm'
	
	x2 = myPos.position()[1]
	y2 = myPos.position()[2]
	theta1 = trig.theta(x1, y1, x2, y2)
#	print'Theta 1:',theta1
	x1 = x2
	y1 = y2
	theta2 = trig.theta(x2, y2, xFinal, yFinal)
#	print'Theta 2:', theta2
	theta = theta2 - theta1
	print'Difference of Thetas:', theta