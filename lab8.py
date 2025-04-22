def calculate_z(a):
    if a < 4:
        z = 0.0
        for n in range(1, 11):  # 1..10
            denominator = 1.0
            a_n = 1.0 # a^n
            for _ in range(n):
                a_n *= a
            denominator = a_n - 5
            term = (a * a) / denominator  
            z += term
    else:
        sum_part = 0.0
        for n in range(1, 9):  # 1..8
            numerator = 1.0 
            a_n = 1.0   #a^n
            for _ in range(n):
                a_n *= a
            term = a_n / (2 * n)
            sum_part += term
        z = ((a + 1) / a) * sum_part
    return z

# Пример табулирования функции для a от 1 до 10 с шагом 1
print("a\tZ(a)")
for a in range(1, 11):
    z = calculate_z(a)
    print(f"{a}\t{z:.4f}")  # Вывод с округлением до 4 знаков после запятой