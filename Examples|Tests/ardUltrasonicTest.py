from nanpy import (ArduinoApi, SerialManager)
import time

try:
	connection = SerialManager()
	a = ArduinoApi(connection = connection)
except:
	print("Failed to connect to Arduino.")


trigger = 7
echo = 8

a.pinMode(trigger, a.OUTPUT)
a.pinMode(echo, a.INPUT)

a.digitalWrite(trigger, a.LOW)
print("Waiting for sensor to settle..")
time.sleep(0.5)
print("Calculating distance...")
a.digitalWrite(trigger, a.HIGH)
time.sleep(0.00001)
a.digitalWrite(trigger, a.LOW)
	
while a.digitalRead(echo) == 0:
	startTime = time.time()

while a.digitalRead(echo) == 1:
	endTime = time.time()
	
duration = endTime - startTime
distance = (duration * 34300) /2
print("Distance:", distance, "cm")

