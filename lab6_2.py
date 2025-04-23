#variant 1

s = 0 #sum
x = 1.2
for i in range(11):
    s += (x**(4*i + 1)) / (4*i + 1)
print(s)
