from math import sqrt, pow, acos, degrees
import sys
import time

class Trig():
	def theta(self, xOrig, yOrig, xCurrent, yCurrent):
		self.xDiff = xCurrent- xOrig
		self.yDiff = yCurrent - yOrig
		self.mag = sqrt(pow(self.xDiff, 2) + pow(self.yDiff, 2))
		if self.mag == 0:
			self.mag = 0.00001
		ang = degrees(acos(self.xDiff/self.mag))
		return ang

