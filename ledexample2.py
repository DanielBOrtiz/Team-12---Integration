import RPi.GPIO as IO # this line imports the necessary libraries and saves them as IO
import time # imports time libraries so we can use the sleep functions

IO.setwarnings(False) # ignore inital warnings
IO.setmode(IO.BCM)
IO.setup(18, IO.OUT) # setup pin 18 as an output pin

p = IO.PWM(18, 200) # setup PWM out of pin 18 with frequency of 200
p.start(0) # start PWM with Duty Cycle of 0

while 1: # puts us in an infinite loop
	for x in range(50):
		p.ChangeDutyCycle(x) # this part of the loop makes the LED go from dim to bright
		time.sleep(0.1)	# duty cycle in this case changes the intensity of the brightness of the LED

	for x in range(50):
		p.ChangeDutyCycle(50-x) # this part of the loop makes the LED go from bright to dim
		time.sleep(0.1)


