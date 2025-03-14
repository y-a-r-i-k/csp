import math

#variant 6

a, b = map(int, input().split())

#calc x:
x = ((a + b) / (1 + a))**1/5

print(x)

#calc z:
z = math.exp((x - 1)**0.5)

#calc y:
y = (2 * math.sin(x) + math.cos(x/2) / (3 + math.cos(x)**2))

print(x, y, z)