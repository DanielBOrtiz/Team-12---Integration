from Navigation import Navigation
from math import fabs
from trig import Trig
import sys
from time import sleep

addr = input("Who is we?")
nav = Navigation(addr)
myPos = nav.position()
trig = Trig()

while True:
	try:
		myPos
		print(myPos)
	except KeyboardInterrupt:
		sys.exit()