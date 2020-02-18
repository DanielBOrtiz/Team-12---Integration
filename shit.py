from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#some = serial_manager()

#serial_manager.connect('/dev/ttyUSB0', 9600)

try:
	connection = SerialManager(device='/dev/ttyUSB0') # The input to 
	# serialmanager is the manual way of setting the connection for the 
	# Arduino. This must be used if we wanna connect the beacon to the Pi
	a = ArduinoApi(connection = connection)
	print'Communication with Arduino was successful.'
except:
	print'Failed to communicate with Arduino. ):'
