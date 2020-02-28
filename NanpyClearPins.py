## SOMETIMES THE PINS ARE THE ARDUINO ARE LEFT HIGH, THIS PROGRAM MUST BE RUN IN ORDER TO SET ALL THE PINS ON THE BOARD TO LOW STATE

from NanpyConnect import nanpyConnect

a = nanpyConnect()

def clearPins(): #
	inPins = input("Clear pins 2 through: ")

	for x in range(2, inPins):
		a.pinMode(x, a.OUTPUT)
		a.digitalWrite(x, a.LOW)

	print'All pins have been cleared.'