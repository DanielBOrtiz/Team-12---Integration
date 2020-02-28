## MANUAL CONTROL FUNCTION. CAN BE CALLED WITH
# manualControl(arduinoconnection, motorOne, motorTwo)
# ADD MANUAL CONTROL CODE INTO THIS FILE

## IN ORDER FOR THIS FUNCTION TO WORK PROPERLY ONE MUST HAVE ARDUINOCONNECTION AND MOTOR CLASSES AS INPUTS TO THE FUNCTION

import curses
import sys

from time import sleep

def manualControl(arduinoApi, motorOne, motorTwo, MANUAL): # for consistency it'd be nice to keep the convention as motor one being the left motor
	# get the curses screen window
	screen = curses.initscr()
	# turn off input echoing
	curses.noecho()
	# respond to keys immediately (don't wait for enter)
	curses.cbreak()
	# map arrow keys to special values
	screen.keypad(True)
	cnt = 0

	MANUALDRIVE = True

	try:	
   	 	while MANUALDRIVE:
        		char = screen.getch()
			if char == ord('y'):
				cnt = cnt + 1
				screen.addstr(0, 0, 'Y Pressed.    ')
				screen.addstr(1, 0, 'Stopping Rover...     ')
				screen.addstr(1, 0, 'Press again to enable autonomous mode.     ')
				#motorOne.stopAll(arduinoApi)
				#motorTwo.stopAll(arduinoApi)
				#if cnt%2 == 0:
				#	screen.addstr(0, 0, 'Going Auto....     ')
				#	return True
				#	break
				#else:
					#break
					#screen.addstr(0, 0, 'st manu     ')
				# Begin rover movement
				motorOne.directionSet("W", arduinoApi)
				motorTwo.directionSet("W", arduinoApi)
				for x in range(0, 52):
				    motorOne.pwmSet(5*x, arduinoApi)
				    motorTwo.pwmSet(5*x, arduinoApi)
				    sleep(0.01)
				MANUALDRIVE = False
				# shut down cleanly
				curses.nocbreak(); screen.keypad(0); curses.echo()
				curses.endwin()
				return True
				break

			if  cnt%2 == 0:
	        		if char == ord('q'):
					motorOne.stopAll(arduinoApi)
					motorTwo.stopAll(arduinoApi)
					# Begin rover movement
					# motorOne.directionSet("W", arduinoApi)
					# motorTwo.directionSet("W", arduinoApi)
					# for x in range(0, 52):
				   	#	motorOne.pwmSet(5*x, arduinoApi)
				   	#	motorTwo.pwmSet(5*x, arduinoApi)
				    	#	sleep(0.01)
					MANUALDRIVE = False
					# shut down cleanly
					curses.nocbreak(); screen.keypad(0); curses.echo()
					curses.endwin()
	        			break

	      	 		elif char == ord('d'): # right
					screen.addstr(0, 0, 'Right Turn    ')
					motorOne.directionSet("W", arduinoApi)
					motorTwo.directionSet("S", arduinoApi)
					for x in range(0, 52):
						motorOne.pwmSet(5*x, arduinoApi)
						motorTwo.pwmSet(5*x, arduinoApi)
						sleep(0.002)

	      		  	elif char == ord('a'): # left
	        			screen.addstr(0, 0, 'Left Turn     ')
					motorOne.directionSet("S", arduinoApi)
					motorTwo.directionSet("W", arduinoApi)
					for x in range(0, 52):
						motorOne.pwmSet(5*x, arduinoApi)
						motorTwo.pwmSet(5*x, arduinoApi)
						sleep(0.002)

	        		elif char == ord('w'): # forwards
	        			screen.addstr(0, 0, 'Forwards     ')
					motorOne.directionSet("W", arduinoApi)
					motorTwo.directionSet("W", arduinoApi)
					for x in range(0, 52):
						motorOne.pwmSet(5*x, arduinoApi)
						motorTwo.pwmSet(5*x, arduinoApi)
						sleep(0.002)

		      	 	elif char == ord('s'): # backwards
	       		 		screen.addstr(0, 0, 'Reverse     ')
					motorOne.directionSet("S", arduinoApi)
					motorTwo.directionSet("S", arduinoApi)
					for x in range(0, 52):
						motorOne.pwmSet(5*x, arduinoApi)
						motorTwo.pwmSet(5*x, arduinoApi)
						sleep(0.002)
				elif char == ord('e'): # stop
					screen.addstr(0, 0, 'Stop     ')
					motorOne.stopAll(arduinoApi)
					motorTwo.stopAll(arduinoApi)
				

			else:	
				screen.addstr(0, 0, 'now auto   ')
	except KeyboardInterrupt:
		# shut down cleanly
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()
		sys.exit()
		motorOne.stopAll(arduinoApi)
		motorTwo.stopAll(arduinoApi)
		MANUALDRIVE = False
		# Begin rover movement
		#motorOne.directionSet("W", arduinoApi)
		#motorTwo.directionSet("W", arduinoApi)
		#for x in range(0, 52):
		#    motorOne.pwmSet(5*x, arduinoApi)
		#    motorTwo.pwmSet(5*x, arduinoApi)
		#    sleep(0.01)
		


