from nanpy import (ArduinoApi, SerialManager)
from time import sleep

ledPin = 7
buttonPin = 8
ledState = False
buttonState = 0

try:
	connection = SerialManager()
	a = arduinoAPI(connection = connection)
except:
	print("Failed to connect to Arduino.")

# Setting up pin modes as if we were in Arduino IDE
a.pinMode(ledPin, a.OUTPUT)
a.pinMode(buttonPin, a.INPUT)
while True:

