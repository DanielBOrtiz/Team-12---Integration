import RPi.GPIO as IO
from time import sleep

while True:
	userIn = raw_input()
	if userIn == 'q' or userIn == 'Q':
		break
	if userIn.isdigit():
		num = int(userIn) 
		for x in range(0, num + 1, int(num/10)):
			print(x)
			sleep(0.1)
	else:
		print("Hello")

