from Position import currentpos
from Ultrasonic import Ultrasonic
import sys
from time import sleep
	
addr = input("Who is we?")
myPos = currentpos(addr)
uSensor = Ultrasonic(11, 13)
uSensor.trigsettle()

while True:
	
	myPos.position()
	sleep(.5)
	print'X: ', myPos.position()[1], 'Y: ', myPos.position()[2]
	print(uSensor.ping())
	sleep(1)
