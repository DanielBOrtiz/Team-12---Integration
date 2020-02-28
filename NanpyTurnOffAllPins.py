from NanpyConnect import nanpyConnect


a = nanpyConnect()

b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13


a.pinMode(b, a.OUTPUT)
a.pinMode(c, a.OUTPUT)
a.pinMode(d, a.OUTPUT)
a.pinMode(e, a.OUTPUT)
a.pinMode(f, a.OUTPUT)
a.pinMode(g, a.OUTPUT)
a.pinMode(h, a.OUTPUT)
a.pinMode(i, a.OUTPUT)
a.pinMode(j, a.OUTPUT)
a.pinMode(k, a.OUTPUT)
a.pinMode(l, a.OUTPUT)
a.pinMode(m, a.OUTPUT)


a.digitalWrite(b, a.LOW)
a.digitalWrite(c, a.LOW)
a.digitalWrite(d, a.LOW)
a.digitalWrite(e, a.LOW)
a.digitalWrite(f, a.LOW)
a.digitalWrite(g, a.LOW)
a.digitalWrite(h, a.LOW)
a.digitalWrite(i, a.LOW)
a.digitalWrite(j, a.LOW)
a.digitalWrite(k, a.LOW)
a.digitalWrite(l, a.LOW)
a.digitalWrite(m, a.LOW)

print'All pins have been cleared.'