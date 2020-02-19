from nanpy import (ArduinoApi, SerialManager)
from time import sleep

try:
	connection = SerialManager(device='/dev/ttyUSB0') # must manually set port
	a = ArduinoApi(connection = connection)
	print'Connection to Arduino was successful!'
	sleep(1)
except:
	print'Failed to Connect to Arduino. :('