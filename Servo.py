## STILL A WORK IN PROGRESS BUT THIS WORKS
# SERVO CLASS TAKES IN A PIN NUMBER AS AN INPUT AND CHANGES THE DUTY CYCLE OF THE SERVO BASED ON SERVO.TURN
# EXAMPLE CODE BELOW

####
#import RPi.GPIO as IO
#from Servo import Servo #from servo file import the servo class
#import time

#servo = Servo(15)
#userIn = input("Cycle: ")
#servo.turn(userIn)
#while True:
#	userIn = input("Duty Cycle: ")
#	if type(userIn) == float or type(userIn) == int and 0 <= userIn < 100 and 0.0 <= userIn < 100.0:
#		servo.turn(userIn)
#IO.cleanup()



import RPi.GPIO as IO
from time import sleep
import sys

IO.setmode(IO.BOARD)
IO.setwarnings(False)

class Servo():
	def __init__(self, sigPin):
		self.sigPin = sigPin
		IO.setup(self.sigPin, IO.OUT)
		self.pwm = IO.PWM(self.sigPin, 200)
		self.pwm.start(8.5)

	def straight(self):
		self.pwm.ChangeDutyCycle(31)

	def turn(self, newCycle):
		self.pwm.ChangeDutyCycle(newCycle)
		
