from Position import currentpos
import RPi.GPIO as IO
from time import sleep

addr = input("Who is we?")
myPos = currentpos(addr)

while True:
	myPos.position()
	sleep(.5)
	print'X:',myPos.position()[1], 'Y',myPos.position()[2]	