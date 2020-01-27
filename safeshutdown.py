from gpiozero import button
import time
import os

stopButton = Button(26) # GPIO 26 as button pin

while True:
	if stopButton.is_pressed: # button press check
	time.sleep(1)
	if stopButton.is_pressed: # check if button is let go
		os.system("shutdown now -h") # -r will reset the pi
	time.sleep(1)
