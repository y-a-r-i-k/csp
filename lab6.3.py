#variant 23
                                                            
def f(x):
    if x <= -2:
        return 8 / x
    elif -2 < x <= 0:
        return x**3 + 4
    else:  # x > 0
        return 4 / (x**2 + 1)

#Задаем начальные значения для табулирования
x0 = -3  
xn = 3   
h = 1    

sum_y = 0
prod_y = 1
first_value = True  # Флаг для первого значения произведения

print(" x      |   f(x)")
print("---------------------")

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
print("---------------------")
print(f"Сумма значений функции: {sum_y:.4f}")
print(f"Произведение значений функции: {prod_y:.4f}")
