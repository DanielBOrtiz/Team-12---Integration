## NAVIGATION CLASS TO SPIT OUT ULTASONIC SENSOR DISTANCE AND CURRENT POSITION

### EXAMPLE CODE BELOW
#from Ultrasonic import Ultrasonic
#from Navigation import Navigation
#import sys
#from time import sleep

#nav = Navigation(12) # the 12 is the address of our beacon
#while True:
#	print'X:', nav.position()[1]
#	print 'Y:', nav.position()[2]



from marvelmind import MarvelmindHedge
import sys
from time import sleep

class Navigation():
	def __init__(self, addr):
		self.addr = addr
		self.hedge = MarvelmindHedge(tty = "/dev/ttyACM2", adr=self.addr, debug=False) # create MarvelmindHedge thread
		self.hedge.start() # start thread
	
	def position(self):
		try:
			pos = self.hedge.position()
			return pos # spit out the full array returned by the Marvelmindhedge fxn
		except KeyboardInterrupt:
			self.hedge.quit()

	def trigsettle(self, trigPin, echoPin): # call this function only once at the beginning of the code 
		self.trigPin = trigPin
		self.echoPin = echoPin
		IO.setup(self.trigPin, IO.OUT) # set up trigger and echo pins
		IO.setup(self.echoPin, IO.IN)
		IO.output(self.trigPin, IO.LOW)
		print("Waiting for sensor to settle..") # settle the trigger pin just in case its has a high value
		time.sleep(0.25)

	def ping(self):
		print "Calculating distance..."
		IO.output(self.trigPin, IO.HIGH)
		time.sleep(0.00001)
		IO.output(self.trigPin, IO.LOW)

		while IO.input(self.echoPin) == 0: # if echo pin has no received a signal after sending a ping through transmitter, start timer
			startTime = time.time()

		while IO.input(self.echoPin) == 1: # if echo pin receives signal, end timer
			endTime = time.time()

		duration = endTime - startTime # calculate total time signal traveled
		distance = (duration * 34300) /2 # find distance using speed of sound eq and divding by two to account for there and back
#		print("Distance:", distance, "cm")
		return distance # returns this distance in centimeters

