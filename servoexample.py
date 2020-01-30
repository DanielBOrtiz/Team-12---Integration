import RPi.GPIO as IO
from time import sleep
from Tkinter import * 
import sys

IO.setmode(IO.BOARD)
IO.setwarnings(False)

sig = 33

IO.setup(sig, IO.OUT)
pwm = IO.PWM(sig, 150)
pwm.start(8.5) 
# w/ wires away from you, 6.0 means far clockwise, 30 
# means counterclockwise 
		
userIn = input("Desired Duty Cycle: ")
pwm.ChangeDutyCycle(userIn)
while type(userIn) == (float and 6 <= userIn < 31) or (int and 6 <= userIn < 31):
	userIn = input("Duty Cycle: ")
	if userIn == 30:
		for x in range(17, 30, 2):
			pwm.ChangeDutyCycle(x)
			sleep(0.15)
	if userIn == 17.5:
			pwm.ChangeDutyCycle(17.5)
	if userIn == 6:
		for x in range(6, 17, 2):
			pwm.ChangeDutyCycle(23-x)
			sleep(0.15)

pwm.stop()
IO.cleanup()

