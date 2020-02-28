from NanpyConnect import nanpyConnect
from time import sleep

a = nanpyConnect()

A = 2
B = 3

aState = 0
aLastState = 0
counter = 0

a.pinMode(A, a.INPUT)
a.pinMode(B, a.INPUT)

a.digitalRead(A)

aLastState = a.digitalRead(A)


while True:

	try:
		aState = a.digitalRead(A)
		if (aState != aLastState):
			if (a.digitalRead(B) != aState):
				counter = counter + 1
			else:
				counter = counter - 1
		print'Position', counter
		sleep(0.01)
		aLastState = aState
	except KeyboardInterrupt:
		pass

print'Position'
print(counter)
		