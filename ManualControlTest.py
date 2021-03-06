from ManualControl import manualControl
from NanpyConnect import nanpyConnect
from nanpy import (ArduinoApi, SerialManager)
from Navigation import Navigation
from MotorClass import Motor
from Trig import Trig
from math import fabs
from time import sleep
import sys

a = nanpyConnect()

M1En = 3
M1A = 4
M1B = 5
M2En = 11
M2A = 9
M2B = 10

motorK = 2
maxPWM = 255

AUTO = True
MANUAL = True

M1 = Motor("LEFT", M1En, M1A, M1B)
M2 = Motor("RIGHT", M2En, M2A, M2B)

M1.pinSet(a)
M2.pinSet(a)

AUTO = manualControl(a, M1, M2, MANUAL)
M1.stopAll(a)
M2.stopAll(a)
print(AUTO)