import pygame
from time import sleep
import os
from Trig import Trig

pygame.joystick.init()
pygame.joystick.Joystick(0).init()
count = pygame.joystick.Joystick(0).get_init()
pygame.init()
trig = Trig()

while True:

	os.putenv('DISPLAY', ':0.0')
	pygame.init()
	for event in pygame.event.get(): # User did something.
       		#if event.type == pygame.QUIT: # If user clicked close.
            		#done = True # Flag that we are done so we exit this loop.
        	if event.type == pygame.JOYAXISMOTION:
			pass
			#print'Left Joystick Position: ', pygame.joystick.Joystick(0).get_axis(1)
			#print'Right Joystick Position: ', pygame.joystick.Joystick(0).get_axis(4)

	leftJoy = pygame.joystick.Joystick(0).get_axis(1)
	rightJoy = pygame.joystick.Joystick(0).get_axis(4)

	if leftJoy == 0:
		leftJoy = 0
	if rightJoy == 0:
		rightJoy = 0

	leftJoy = leftJoy * -1
	rightJoy = rightJoy * -1

	if leftJoy < 0:
		leftJoy *= -1
		leftJoy = trig.map(leftJoy, 0, 1, 0, 255)
		leftJoy *= -1
	else:
		leftJoy = trig.map(leftJoy, 0, 1, 0, 255)

	if rightJoy < 0:
		rightJoy *= -1
		rightJoy = trig.map(rightJoy, 0, 1, 0, 255)
		rightJoy *= -1
	else:
		rightJoy = trig.map(rightJoy, 0, 1, 0, 255)

	print'Left Joystick Position: ', leftJoy
	print'Right Joystick Position: ', rightJoy
	sleep(0.01)