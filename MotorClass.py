## DUE TO ISSUES WITH THE WHOLE A. STUFF THIS CLASS MUST BE PLACED WITHIN THE FILE THAT CALLS IT
## REFER TO MOTORCONTROL.PY FOR REFERENCE



#from nanpy import (ArduinoApi, SerialManager)
#from NanpyConnect import nanpyConnect
from time import sleep

class Motor():
	def __init__(self, motor, enablePin, aPin, bPin): # Takes in the pins for motor driver
		self.enablePin = enablePin
		self.aPin = aPin
		self.bPin = bPin
		self.motor = motor

	def pinSet(self, a): # Made this function because I was having trouble with self.a
		# Set up of pins specified for motor
		a.pinMode(self.aPin, a.OUTPUT)
		a.pinMode(self.bPin, a.OUTPUT)
		a.pinMode(self.enablePin, a.OUTPUT)

		# Set pins to low states, just in case
		a.digitalWrite(self.aPin, a.LOW)
		a.digitalWrite(self.bPin, a.LOW)
		a.analogWrite(self.enablePin, 0)
		

	def directionSet(self, direction, a): # this function handles the direction of the motor
		self.direction = direction
		if (self.motor == "L" or self.motor == "LEFT"):
			if (self.direction == "forward" or self.direction == "w" or self.direction == "W"):
				a.digitalWrite(self.aPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand
				a.digitalWrite(self.bPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand
				a.digitalWrite(self.aPin, a.HIGH)# CCW
				a.digitalWrite(self.bPin, a.LOW)
				# print(self.motor, self.direction)
				return "w" # return the directions so we can handle it externally
			elif (self.direction == "reverse" or self.direction == "s" or self.direction == "S"): 
				a.digitalWrite(self.aPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand 
				a.digitalWrite(self.bPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand
				a.digitalWrite(self.aPin, a.LOW) # CW
				a.digitalWrite(self.bPin, a.HIGH)
				# print(self.motor, self.direction)
				return "s" # return the directions so we can handle it externally
			else:
				pass
				print'Incorrect direction input.'

		elif (self.motor == "R" or self.motor == "RIGHT"):
			if (self.direction == "forward" or self.direction == "w" or self.direction == "W"): 
				a.digitalWrite(self.aPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand
				a.digitalWrite(self.bPin, a.LOW) # set pins to low state just in case we have some pins as high beforehand
				a.digitalWrite(self.aPin, a.LOW) # CW
				a.digitalWrite(self.bPin, a.HIGH)
				# print(self.motor, self.direction)
				return "w" # return the directions so we can handle it externally
			elif (self.direction == "reverse" or self.direction == "s" or self.direction == "S"): 
				a.digitalWrite(self.aPin, a.LOW)
				a.digitalWrite(self.bPin, a.LOW)
				a.digitalWrite(self.aPin, a.HIGH) # CCW
				a.digitalWrite(self.bPin, a.LOW)
				# print(self.motor, self.direction)
				return "s" # return the directions so we can handle it externally
			else:
				print'Incorrect direction input.'
		else:
			print'Incorrect motor.'

	def pwmSet(self, pwm, a): # this function handles the speed of the motor
		self.pwm = pwm
		a.analogWrite(self.enablePin, pwm) # simply writes that pwm as an analog signal
		return pwm # make sure to return the pwm that way we can check it beforehand
	
	def stopAll(self,a): # this function sets all pins to low
		# Turn off all pins
		a.digitalWrite(self.aPin, a.LOW)
		a.digitalWrite(self.bPin, a.LOW)
		a.analogWrite(self.enablePin, 0)

		
