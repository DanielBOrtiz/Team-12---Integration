import RPi.GPIO as IO
from time import sleep

while True:
	userIn = raw_input()
	if userIn == 'q' or userIn == 'Q':
		break
	if userIn.isdigit():
		num = int(userIn) 
		print(num)
		sleep(0.1)
		continue
	if userIn == 'w' or userIn == 'W':
		print("Forward")
		continue
	if userIn == 's' or userIn == 's':
		print("Reverse")
		continue
	if userIn == 'd' or userIn == 'D':
		print("Right")
		continue
	if userIn == 'a' or userIn == 'A':
		print("Left")
		continue
