import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

# Motor 1 pin declarations
M1A = 11
M1B = 13
M1En = 12
# Motor 2 pin declarations
M2A = 22
M2B = 24
M2En = 23

# Set up pins as outputs
IO.setup(M1A, IO.OUT)
IO.setup(M1B, IO.OUT)
IO.setup(M1En, IO.OUT)
IO.setup(M2A, IO.OUT)
IO.setup(M2B, IO.OUT)
IO.setup(M2En, IO.OUT)

# Set PWM pins to output PWM w/ 200 Hz frequency
pwm1 = IO.PWM(M1En, 200)
pwm2 = IO.PWM(M2En, 200)

# Backwards, Out1 to +, Out2 to -, right motor
# Backwards, Out3 to -, Out4 o +, left motor 
# These configs are with the Enable and PWM pins on the Driver far from you
pwm1.start(80)
IO.output(M1A, IO.LOW)
IO.output(M1B, IO.HIGH)
pwm2.start(80)
IO.output(M2A, IO.LOW)
IO.output(M2B, IO.HIGH)
time.sleep(4)

pwm1.stop()
pwm2.stop()
time.sleep(1)

# Forward
pwm1.start(50)
pwm2.start(50)
IO.output(M1A, IO.HIGH)
IO.output(M1B, IO.LOW)
IO.output(M2A, IO.HIGH)
IO.output(M2B, IO.LOW)
time.sleep(4)

pwm1.stop()
IO.cleanup()

