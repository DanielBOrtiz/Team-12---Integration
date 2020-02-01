import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

#testPin = 12 # temp
#IO.setup(testPin, IO.OUT) # temp 

class  motor:
	pwm = 0; # set pwm as zero
	drxn = "" # empty character as direction

	if drxn == 'w' or drxn == 'W':
		drxn = "Counteclockwise" # if user enters this key change the string in "direction" to "Forward"
	if drxn == 's' or drxn == 'S':
		drxn = "Clockwise"
	if drxn == 'd' or drxn == 'D':
		drxn = "Clockwise"
	if drxn == 'a' or drxn == 'A':
		drxn = "Counterclockwise"
	if pwm >= 0:
		pwm = int(pwm)
	def desc(self):
		if self.pwm < 0:
			self.pwm = 12
		descStr = "PWM is %f, direction is %s" % (self.pwm, self.drxn)
		return descStr # return string with pwm and direction

while True:
	userIn = raw_input()
	M1 = motor()
	if userIn != 'q' or userIn != 'Q':
		M1.drxn = userIn
		print(M1.desc())
		continue
	if type(userIn) == int:
		num == int(userIn)
		M1.pwm = num
		M1.drxn = userIn
		print(M1.desc())
		continue
	if userIn == 'q' or userIn == 'Q':
		break


