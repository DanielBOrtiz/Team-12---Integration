from math import sqrt, pow, acos, degrees, fabs
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
	
	def magnitude(self, xCurrent, yCurrent, xFinal, yFinal):
		xMagDiff = xFinal - xCurrent
		yMagDiff = yFinal - yCurrent
		mag = sqrt(pow(xMagDiff, 2) + pow(yMagDiff, 2))
		return mag

	## MAPS LEFT VALUES TO RIGHT VALUES BASED ON VALUE = VALUE
	## I.E if value = 50 and left is 0 to 100 and right is 0 to 255, output is 128.
		
	def map(self, value, leftMin, leftMax, rightMin, rightMax):
		# Figure out how 'wide' each range is
		leftSpan = leftMax - leftMin
		rightSpan = rightMax - rightMin

	   	# Convert the left range into a 0-1 range (float)
	 	valueScaled = float(value - leftMin) / float(leftSpan)

    	# Convert the 0-1 range into a value in the right range.
    		return round(rightMin + (valueScaled * rightSpan)) # returns float, turn into int, comma after value will give number of decimals to round to
    
		## MAPS LEFT VALUES TO RIGHT VALUES BASED ON VALUE = VALUE


