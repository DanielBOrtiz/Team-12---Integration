## THE FOLLLOWING CODE TAKES INPUT JOYSTICKAXIS AND RETURNS THAT AXIS VALUE USING PYGAME

## EXAMPLE BELOW ON HOW TO USE THIS FUNCTION

#from PygameControllerConnect import psControl
#from time import sleep

#ps = psControl()


#while True:
#	try:
#		sleep(0.01)
#		leftJoy = ps.joyStick(1)
#		rightJoy = ps.joyStick(4)
#		print'Left Joystick: ', leftJoy
#		print'Right Joystick: ', rightJoy
#		xButton = ps.buttonPress(0)
#		oButton = ps.buttonPress(1)
#		tButton = ps.buttonPress(2)
#		sButton = ps.buttonPress(3)
#		if xButton == 1:
#			print'CROSS Button Pressed.'
#			sleep(0.1) # debounce
#		if oButton == 1:
#			print'CIRCLE Button Pressed.'
#			sleep(0.1) # debounce
#		if tButton == 1:
#			print'TRIANGLE Button Pressed.'
#			sleep(0.1) # debounce
#		if sButton == 1:
#			print'SQUARE Button Pressed.'
#			sleep(0.1) # debounce
#
#	except KeyboardInterrupt:
#		break

import pygame
import os
from Trig import Trig


class psControl():
	def __init__(self):
		os.putenv('DISPLAY', ':0.0') # LINE SO WE DON'T HAVE TO CREATE WINDOW
		pygame.joystick.init() # INITIALIZE JOYSTICK
		pygame.joystick.Joystick(0).init() # INITIALIZE JOYTSICK 0, CORRESPONDS TO THE CONTROL'S 2 JOYSTICKS
		self.trig = Trig()

	def joyStick(self, joystickAxis):
		pygame.init()# INITIALIZE PYGAME
		for event in pygame.event.get(): # LISTENER TO LISTEN FOR EVENT.
        		if event.type == pygame.JOYAXISMOTION: # LISTEN FOR EVENT JOYSTICK AXIS MOTION
				pass ## TRIED TO DO PRINT STATEMENTS HERE, WAY TOO FAST.

		joystick = pygame.joystick.Joystick(0).get_axis(joystickAxis) # SET JOYSTICKAXIS AS JOYSTICK THAT THIS FUNCTION WILL RRETURN 


		joystick = joystick * -1 # FOR SOME REASON UP IS NEGATIVE SO WE'LL FLIP THE SIGN CONVENTION
		if joystick == 0: # THE COMMAND ABOVE WOULD YIELD A NEGATIVE ZERO, THIS WILL SET NEGATIVE EQUAL TO ZERO IF CURRENT AXIS VALUE IS ZERO
			joystick = 0

		if joystick < 0: # IF THE USER PULLS BACK ON THE JOYSTICK
			joystick *= -1 # MAKE THE VALUE POSITIVE TO MAP TO PWM RANGE 0-255
			joystick = self.trig.map(joystick, 0, 1, 0, 255) # MAP THAT NUMBER TO A RANGE FROM 0-255 WHICH CORRESPOND TO PWM FOR ARDUINO
			joystick *= -1 # MAKE THE VALUE NGEATIVE AGAIN
		else:
			joystick = self.trig.map(joystick, 0, 1, 0, 255) # IF THE VALUE ISN'T ALREADY NEGATIVE JUST MAP IT TO THE PWM RANGE
	
		#print'Left Joystick Position: ', joystick # TEST LINE TO PRINT JOYSTICK VALUE
		return joystick # RETURN JOYSTICK VALUE TO BE USED IN MAIN CODE

	def buttonPress(self, buttonNum):
		pygame.init()
		for event in pygame.event.get(): # LISTENER TO LISTEN FOR EVENT.
        		if event.type == pygame.JOYAXISMOTION: # LISTEN FOR EVENT 
				pass ## TRIED TO DO PRINT STATEMENTS HERE, WAY TOO FAST.

		buttonState = pygame.joystick.Joystick(0).get_button(buttonNum) # CROSS is button 0, CIRCLE is button 1, TRIANGLE is button 2, SQUARE is button 3
		return buttonState # BUTTONSTATE WILL RETURN 0 OR 1


