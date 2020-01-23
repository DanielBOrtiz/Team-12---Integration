import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(03, IO.OUT)
IO.setup(05, IO.OUT)
IO.setup(07, IO.OUT)

pwm = IO.PWM(07, 100)
pwm.start(0)

IO.output(03, True)
IO.output(05, False)
pwm.ChangeDutyCycle(50)
IO.output(07, True)
time.sleep(2)
IO.output(07, False)

IO.output(03, False)
IO.output(05, True)
pwm.ChangeDutyCycle(75)
IO.output(07, True)
time.sleep(3)
IO.output(07, False)

pwm.stop()
IO.cleanup()

