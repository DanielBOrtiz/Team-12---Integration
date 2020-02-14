from trig import Trig
import sys
import time
import serial

port1 = "/dev/ttyUSB0"

a = serial.Serial(port1, 9600)
a.write('255, 255,')
time.sleep(2)
m