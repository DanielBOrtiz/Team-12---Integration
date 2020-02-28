## THE FOLLOWING FUNCTION WAS USED TO DERIVE PYGAMECONTROLTEST.PY

import pygame
from time import sleep
import os
from Trig import Trig

def psControl(leftJoystick, rightJoystick):

	pygame.joystick.init()
	pygame.joystick.Joystick(0).init()
	pygame.init()
	trig = Trig()

	os.putenv('DISPLAY', ':0.0')
	pygame.init()
	for event in pygame.event.get(): # User did something.
        	if event.type == pygame.JOYAXISMOTION:
			pass

	leftJoy = pygame.joystick.Joystick(0).get_axis(leftJoystick)
	rightJoy = pygame.joystick.Joystick(0).get_axis(rightJoystick)

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

while True:

	joystick = psControl(1, 4)