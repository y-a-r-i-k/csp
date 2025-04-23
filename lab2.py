import math

#variant 6

a, b = map(int, input().split())

#calc x:
try:
    x = math.pow((a + b) / (1 + a), 1/5)
    
except ZeroDivisionError:
    print("b argument's probably too small")

#calc z:
z = math.exp((x - 1)**0.5)

#calc y:
y = (2 * math.sin(x) + math.cos(x/2) / (3 + math.cos(x)**2))

print(x, y, z)