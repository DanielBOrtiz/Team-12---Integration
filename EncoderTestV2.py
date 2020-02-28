from NanpyConnect import nanpyConnect
from gpiozero import DigitalInputDevice
from time import sleep

class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        encoder = DigitalInputDevice(pin)
        encoder.when_activated = self._increment
        encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0
    def _increment(self):
        self._value += 1
    @property
    def value(self):
        return self._value


e1 = Encoder(17)

while True:
    print("e1 {}".format(e1.value))
    sleep(0.5)