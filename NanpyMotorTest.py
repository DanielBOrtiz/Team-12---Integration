from nanpy import (ArduinoApi, SerialManager)
from time import sleep

try:
	connection = SerialManager(device='/dev/ttyUSB0')
	a = ArduinoApi(connection = connection)
	print'Communication with Arduino was successful.'
except:
	print'Failed to communicate with Arduino. ):'

M1A = 4
M1B = 7
M2A = 12
M2B = 13
a.pinMode(M1A, a.OUTPUT)
a.pinMode(M1B, a.OUTPUT)
a.pinMode(M2A, a.OUTPUT)
a.pinMode(M2B, a.OUTPUT)
a.digitalWrite(M1A, a.LOW)
a.digitalWrite(M2B, a.LOW)
a.digitalWrite(M2A, a.LOW)
a.digitalWrite(M2B, a.LOW)

M1En = 5
M2En = 6
a.pinMode(M1En, a.OUTPUT)
a.pinMode(M2En, a.OUTPUT)
a.analogWrite(M1En, 0)
a.analogWrite(M2En, 0)

try:
	print'Turning Motor 1'

	print'Clockwise'
	sleep(2)
	for x in range(0, 255):
		a.analogWrite(M1En, x)
		a.digitalWrite(M1A, a.HIGH)
		print(x)
		sleep(0.01)
	for x in range(0, 255):
		a.analogWrite(M1En, 255-x)
		print(255-x)
		sleep(0.01)

	a.digitalWrite(M1A, a.LOW)
	a.analogWrite(M1En, 0)

	print'Counterclockwise'
	sleep(2)
	for x in range(0, 255):
		a.analogWrite(M1En, x)
		a.digitalWrite(M1B, a.HIGH)
		print(x)
		sleep(0.01)
	for x in range(0, 255):
		a.analogWrite(M1En, 255-x)
		print(255-x)
		sleep(0.01)

	a.digitalWrite(M1B, a.LOW)
	a.analogWrite(M1En, 0)
	
	print'Turning Motor 2'
	print'Clockwise'
	sleep(2)
	for x in range(0, 255):
		a.analogWrite(M2En, x)
		a.digitalWrite(M2A, a.HIGH)
		print(x)
		sleep(0.01)
	for x in range(0, 255):
		a.analogWrite(M2En, 255-x)
		print(255-x)
		sleep(0.01)

	a.digitalWrite(M2A, a.LOW)
	a.analogWrite(M2En, 0)

	print'Counterclockwise'
	sleep(2)
	for x in range(0, 255):
		a.analogWrite(M2En, x)
		a.digitalWrite(M2B, a.HIGH)
		print(x)
		sleep(0.01)
	for x in range(0, 255):
		a.analogWrite(M2En, 255-x)
		print(255-x)
		sleep(0.01)

	a.digitalWrite(M2B, a.LOW)
	a.analogWrite(M2En, 0)
	a.digitalWrite(M1A, a.LOW)
	a.digitalWrite(M2B, a.LOW)
	a.digitalWrite(M2A, a.LOW)
	a.digitalWrite(M2B, a.LOW)
	a.analogWrite(M1En, 0)
	a.analogWrite(M2En, 0)

except KeyboardInterrupt:
	a.digitalWrite(M1A, a.LOW)
	a.digitalWrite(M2B, a.LOW)
	a.digitalWrite(M2A, a.LOW)
	a.digitalWrite(M2B, a.LOW)
	a.analogWrite(M1En, 0)
	a.analogWrite(M2En, 0)
