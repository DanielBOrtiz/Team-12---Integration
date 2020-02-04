## BELOW IS A BASIC IMPLEMENTATION OF PWM WITH A CYTRON MOTOR DRIVER
# NOTICE HOW THIS ONE OPERATES WITH A DIRECTION PIN AND PWM PIN INSTEAD OF AN ON-OFF 
# CONFIGURATION TO SET THE DIRECTION OF MOTOR SPIN

import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setwarnings(False)

class SpeedCount():
	def __init__(self):
		self.x = 50
	
	def increment(self):
		if(self.x < 100):
			self.x = self.x + 1
		else:
			print('max speed reached')
	
	def decrement(self):
		if(self.x > 0):
			self.x = self.x - 1
		else:
			print('minimum speed reached')	


pwm = 11
dir = 13

IO.setup(dir, IO.OUT)
IO.setup(pwm, IO.OUT)

pwm = IO.PWM(pwm, 200)

pwm.start(0)
IO.output(dir, IO.HIGH) # high direction pin turns motor counterclockwise

for x in range(0, 100, 5):
	pwm.ChangeDutyCycle(x)
	print(x)
	time.sleep(1.5)

IO.cleanup()
