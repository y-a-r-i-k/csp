#v2
def calc_z(a):
    if a < 4:
        z = 0.0
        for n in range(1, 11):  # 1..10
            d = 1.0
            a_n = 1.0 # a^n
            for _ in range(n):
                a_n *= a
            d = a_n - 5
            term = (a * a) / d  
            z += term
    else:
        sum_part = 0.0
        for n in range(1, 9):  # 1..8
            a_n = 1.0   #a^n
            for _ in range(n):
                a_n *= a
            term = a_n / (2 * n)
            sum_part += term
        z = ((a + 1) / a) * sum_part
    return z

x0 = float(input())
xh = float(input())
xn = float(input())

x = x0
while x <= xn:
    z = calc_z(x)
    print(f"{x}\t{z:.4f}")
    x += xh