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
	a.digitalWrite(ledPin, a.HIGH)
	ledState = True
	print("LED ON")
	sleep(1)
	a.digitalWrite(ledPin, a.LOW)
	ledState = False
	print("LED  OFF")
	sleep(1)
	a.digitalWrite(ledPin, a.HIGH)
	ledState = True
	print("LED ON")
	sleep(1)
