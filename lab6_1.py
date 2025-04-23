#variant 1

n = int(input(""))

s = 0
for i in range(1, n + 1):
    e = 1/(i**2)
    s += e
    print(f"a{i}={e}")

print(s)