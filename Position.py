## SPITS OUT X AND Y COORDINATE OF BEACON POSITION
## EXAMPLE CODE BELOW

####
#from Position import currentpos
#addr = input("Who is we?")
#myPos = currentpos(addr)

#while True:
#	myPos.position()
#	sleep(.5)
#	print'X:',myPos.position()[1], 'Y',myPos.position()[2]

from marvelmind import MarvelmindHedge
import sys
from time import sleep


class currentpos():
	def __init__(self, addr):
		self.addr = addr
		self.hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=self.addr, debug=False) # create MarvelmindHedge thread
		self.hedge.start() # start thread

	def position(self):
		pos = self.hedge.position()
#		sleep(0.5)
#		print("X:", pos[1], "Y: ", pos[2])
		return pos # spit out the full array returned by the Marvelmindhedge fxn
