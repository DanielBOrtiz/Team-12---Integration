## MANUAL CONTROL FUNCTION. CAN BE CALLED WITH
# manualControl()
# ADD MANUAL CONTROL CODE INTO THIS FILE



import curses

def manualControl():
	# get the curses screen window
	screen = curses.initscr()
	# turn off input echoing
	curses.noecho()
	# respond to keys immediately (don't wait for enter)
	curses.cbreak()
	# map arrow keys to special values
	screen.keypad(True)
	cnt = 0

	try:	
   	 while True:
        	char = screen.getch()
		if char == ord('y'):
			cnt = cnt + 1
			if cnt%2 == 1:
				screen.addstr(0, 0, 'st auto   ')
			else:
				screen.addstr(0, 0, 'st manu   ')
		if  cnt%2 == 0:
	        	if char == ord('q'):
	        		break
	      	 	elif char == ord('d'): # right
	        		# print doesn't work with curses, use addstr instead
				#print('d')
	        		screen.addstr(0, 0, "right    ")
	      	  	elif char == ord('a'): # left
	        		screen.addstr(0, 0, 'left     ')
	        	elif char == ord('w'): # forwards
	        		screen.addstr(0, 0, 'forwards  ')
	      	 	elif char == ord('s'): # backwards
	        		screen.addstr(0, 0, 'backwards ')
			elif char == ord('e'): # stop
				screen.addstr(0, 0, 'stop     ')
		else:	
			screen.addstr(0, 0, 'now auto   ')
	finally:
		# shut down cleanly
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()

