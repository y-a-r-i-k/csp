#variant 1
def mymax(a, b):
    if a > b:
        m = a
    else:
        m = b
    return m

x1, x2, x3, x4 = map(int, input().split())
a = mymax(x1, x2)
b = mymax(x3, x4)
print(mymax(a, b))
