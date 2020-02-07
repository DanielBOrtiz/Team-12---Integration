from Position import currentpos
from Ultrasonic import Ultrasonic
import sys
from time import sleep

class Navigation():
	def __init__(self, addr):
		self.addr = addr
		self.uSensor = Ultrasonic(11, 13)
		self.uSensor.trigsettle()

	def getpos(self):
		position = currentpos(self.addr)
		return position

	def getdist(self):
		distance = self.uSensor
		return distance

nav = navigation(12)
print(nav.getpos()[1])