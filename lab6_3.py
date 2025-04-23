#variant 23
                                                            
def f(x):
    if x <= -2:
        res = 8 / x
    elif -2 < x <= 0:
        res =  x**3 + 4
    else:  # x > 0
        res = 4 / (x**2 + 1)
    return res

#Задаем начальные значения для табулирования
x0 = int(input()) 
xn = int(input())   
h = int(input())

sum_y = 0
prod_y = 1
first_value = True  # Флаг для первого значения произведения

# Цикл для табулирования
for x in range(x0, xn + 1, h):
    y = f(x)
    print(f"{x:<8} | {y:.4f}")
    
    sum_y += y
    
    if first_value:
        prod_y = y  # Устанавливаем первое значение произведения
        first_value = False
    else:
        prod_y *= y  # Умножаем на текущее значение

# Вывод суммы и произведения
print(f"Сумма: {sum_y:.4f}")
print(f"Произведение: {prod_y:.4f}")
