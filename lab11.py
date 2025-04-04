#variant 1

l = int(input())
t = tuple(int(input()) for _ in range(l))
n = int(input())

is_in_tuple = False
for i in range(l):
    for j in range(l):
        if t[i] * t[j] == n and i != j:
            is_in_tuple = True

print("Да" if is_in_tuple else "Нет")