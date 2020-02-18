class Motor():
	from nanpy import (ArduinoApi, SerialManager)
	from time import sleep
	def __init__(self, enablePin, aPin, bPin): # Takes in the pins for motor driver

		try:
			connection = SerialManager(device='/dev/ttyUSB0') # must manually set port
			self.a = ArduinoApi(connection = connection)
			print'Connection to Arduino was successful!'
			sleep(1) 
		except:
			print'Failed to Connect to Arduino. :('

		# Set up of pins specified for motor
		self.a.pinMode(self.aPin, a.OUTPUT)
		self.a.pinMode(self.bPin, a.OUTPUT)
		self.a.pinMode(self.enablePin, a.OUTPUT)
		self.a.digitalWrite(self.aPin, a.LOW)
		self.a.digitalWrite(self.bPin, a.LOW)
		a.analogWrite(self.enablePin, 0)

	def directionSet(self, direction): # this function handles the direction of each motor
		if (self.direction == "forward" or self.direction == "w" or self.direction == "W"): # Forward for left motor is CCW
			self.a.digitalWrite(self.aPin, a.LOW)
			self.a.digitalWrite(self.bPin, a.HIGH)
			return "w"
		elif (self.direction == "reverse" or self.direction == "s" or self.direction == "S"): # Reverse for left motor is CW
			self.a.digitalWrite(self.aPin, a.HIGH)
			self.a.digitalWrite(self.bPin, a.LOW)
			return "s"

	def pwmSet(self, pwm): # this function handles the speed of the motor
		self. pwm = pwm
		self.a.analogWrite(self.enablePin, pwm)
		return pwm
		
