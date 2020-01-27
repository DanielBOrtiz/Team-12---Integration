import RPi.GPIO as IO
from time import sleep
from Tkinter import * 
import sys

IO.setmode(IO.BOARD)
IO.setwarnings(False)

sig = 11

IO.setup(sig, IO.OUT)
pwm = IO.PWM(sig, 200)
pwm.start(8.5) 
# w/ wires away from you, 7 means far clockwise, 40 (or about 38)
# means counterclockwise 
		
userIn = input("Desired Duty Cycle: ")
pwm.ChangeDutyCycle(userIn)
while type(userIn) == int and 6 < userIn < 42:
	userIn = input("Duty Cycle: ")
	pwm.ChangeDutyCycle(userIn)


pwm.stop()
IO.cleanup()

