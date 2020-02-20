from Position import currentpos
from time import sleep
from Navigation import Navigation

nav = Navigation()
nav.position()

while True:
	nav.position()
    	sleep(.1)
   	print'X:',nav.position()[1], 'Y', nav.position()[2]  