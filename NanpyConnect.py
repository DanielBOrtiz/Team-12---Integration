from nanpy import (ArduinoApi, SerialManager)

def nanpyConnect():
	# Manually ask the user to enter port number for Arduino
	#num = input("What port is Arduino plugged in to?: ")
	#port = '/dev/ttyACM' + str(num)

	try:
		connection = SerialManager(device='/dev/ttyUSB-ArduinoMEGA')
		a = ArduinoApi(connection = connection)
		print'Arduino communication was successful.'
		return a
	except:
		print'Unable to communicate with Arduino.'

