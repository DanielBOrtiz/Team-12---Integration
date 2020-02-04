import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

TRIGGER = 11
ECHO = 13

IO.setup(TRIGGER, IO.OUT)
IO.setup(ECHO, IO.IN)

IO.output(TRIGGER, IO.LOW)
print "Waiting for sensor to settle.."
time.sleep(2)

while True:
	print "Calculating distance..."
	IO.output(TRIGGER, IO.HIGH)
	time.sleep(0.00001)
	IO.output(TRIGGER, IO.LOW)

	while IO.input(ECHO) == 0:
		startTime = time.time()

	while IO.input(ECHO) == 1:
		endTime = time.time()

	duration = endTime - startTime
	distance = (duration * 34300) /2
	print "Distance:", distance, "cm"
	time.sleep(2)

IO.cleanup()

