import RPi.GPIO as IO # import GPIO librery

from time import sleep

IO.setmode(IO.BOARD)
IO.setwarnings(False)

M1A = 11
M1B = 13
M1En = 15

IO.setup(M1A,IO.OUT)
IO.setup(M1B,IO.OUT)

IO.setup(M1En,IO.OUT)

pwm = IO.PWM(M1En, 200)


print "Counterclockwise, Accelerate"
IO.output(M1A,IO.HIGH)
IO.output(M1B,IO.LOW)
pwm.start(0)

for x in range (10, 100):
	pwm.ChangeDutyCycle(x)
	sleep(0.1)
print "Decelerate"
for x in range (10, 100):
	pwm.ChangeDutyCycle(100-x)
	sleep(0.1)

print "Stop"
IO.output(M1A, IO.LOW)
IO.output(M1B, IO.LOW)
pwm.stop()
sleep(0.5)

print "Clockwise, Accelerate"
IO.output(M1B, IO.HIGH)
IO.output(M1A, IO.LOW)
pwm.start(0)

for x in range (10, 100):
	pwm.ChangeDutyCycle(x)
	sleep(0.1)
print "Decelerate"
for x in range (10, 100):
	pwm.ChangeDutyCycle(100-x)
	sleep(0.1)

print "Stop"
IO.output(M1A, IO.LOW)
IO.output(M1B, IO.LOW)
IO.output(M1En, IO.LOW)
pwm.stop()

IO.cleanup()
