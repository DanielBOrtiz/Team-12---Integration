from marvelmind import MarvelmindHedge
import sys
from time import sleep

addr = input("Who is we? ")
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=addr, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread

while True:
	pos = hedge.position()
	sleep(0.5)
	print("X:", pos[1], "Y: ", pos[2])