from nanpy import (ArduinoApi, SerialManager)

def nanpyConnect():
	# Manually ask the user to enter port number for Arduino
	num = input("What port is Arduino plugged in to?: ")
	port = '/dev/ttyUSB' + str(num)

	try:
		connection = SerialManager(device=port)
		a = ArduinoApi(connection = connection)
		print'Arduino communication was successful.'
		return a
	except:
		print'Unable to communicate with Arduino.'

