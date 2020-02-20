from NanpyConnect import nanpyConnect
from time import sleep
from MotorClass import Motor

a = nanpyConnect()
print(a)

M1En = 3
M1A = 7
M1B = 8


M1 = Motor("LEFT", M1En, M1A, M1B)

M1.pinSet(a)

M1.directionSet("W", a)
for x in range(0, 52):
    M1.pwmSet(5*x, a)
    sleep(0.01)
M1.stopAll(a)