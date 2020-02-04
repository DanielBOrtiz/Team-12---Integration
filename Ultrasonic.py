## THIS CLASS TAKES TWO INPUTS, TRIGPIN AND ECHOPIN
## TRIGSETTLE MUST BE CALLED JUST IN CASE THE TRIGGER PIN IS FLOATING
## PING FUNCTION RETURNS THE DISTANCE IN CENTIMETERS

## BELOW IS A BASIC IMPLEMENTATION OF THIS CODE THAT SPITS OUT A DISTANCE EVERY SECOND

#from Ultrasonic import Ultrasonic
#import time
#import RPi.GPIO as IO

#uss = Ultrasonic(11, 13) # setting trigPin and echoPin as 11 and 13, respectively
#uss.trigsettle()
#while True:
#	print("Calculating distance:")
#	print(uss.ping())
#	time.sleep(1)	




import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setwarnings(False)

class Ultrasonic():
	trigPin = 11 # default pins for ultrasonic sensor
	echoPin = 13 # can be changed when calling the Ultrasonic class
	
	def __init__(self, trigPin, echoPin): # set up of all the pins for the sensor
		self.trigPin = trigPin
		self.echoPin = echoPin
		IO.setup(self.trigPin, IO.OUT)
		IO.setup(self.echoPin, IO.IN)

	def trigsettle(self): # only has to be called once to settle trigPin
		IO.output(self.trigPin, IO.LOW)
		print("Waiting for sensor to settle..")
		time.sleep(0.5)

	def ping(self): # function that calculates the distance traveled by the ping
#		print "Calculating distance..."
		IO.output(self.trigPin, IO.HIGH)
		time.sleep(0.00001)
		IO.output(self.trigPin, IO.LOW)

		while IO.input(self.echoPin) == 0:
			startTime = time.time()

		while IO.input(self.echoPin) == 1:
			endTime = time.time()

		duration = endTime - startTime
		distance = (duration * 34300) /2
#		print("Distance:", distance, "cm")
		return distance # returns this distance in centimeters


