import RPi.GPIO as IO
from Servo import Servo #from servo file import the servo class
import time

servo = Servo(36)
userIn = input("Cycle: ")
servo.turn(userIn)
while True:
	userIn = input("Duty Cycle: ")
	if type(userIn) == float or type(userIn) == int and 0 <= userIn < 100 and 0.0 <= userIn < 100.0:
		servo.turn(userIn)
IO.cleanup()