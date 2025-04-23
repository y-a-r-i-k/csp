#variant 1
def f(x):
    if -2 <= x <= -1:
        res = 2 * x + 4
    elif -1 < x <= 1:
        res = 2 * (x ** 2)
    elif 1 < x <= 2:
        res = -2 * x + 2
    else:
        res = "Функция не определена"
    print(res)

inp = int(input())
f(inp)

