from Position import currentpos
from time import sleep
from Navigation import Navigation

addr = input("Who is we?")
nav = Navigation(addr)
nav.position()

while True:
	nav.position()
    	sleep(.5)
   	print'X:',nav.position()[1], 'Y', nav.position()[2]  