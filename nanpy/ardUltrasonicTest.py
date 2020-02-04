from nanpy import ArduinoApi
from nanpy import SerialManager
from nanpy import Ultrasonic
from time import sleep

trigPin = 7
echoPin = 8

try:
	connection = SerialManager()
	a = ArduinoApi(connection = connection)
except:
	print("Failed to connect to Arduino.")

ultrasonic = Ultrasonic(echoPin, trigPin, False, connection=connection)

def test():
    distance = ultrasonic.get_distance()
    if distance < 5:
        print('distance is:')
        print(distance)
        print('too close!')
    sleep(0.002)

while True:
    test()