from Ultrasonic import Ultrasonic
import time
import RPi.GPIO as IO

uss = Ultrasonic(11, 13)
uss.trigsettle()
while True:
	print("Calculating distance:")
	print(uss.ping())
	time.sleep(1)	

