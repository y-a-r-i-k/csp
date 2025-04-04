#variant 9

def cout_negative(l: list) -> int:
    return sum(1 for x in l if x < 0)

def count_positive(l: list) -> int:
    return sum(1 for x in l if x > 0)

def count_zeros(l: list) -> int:
    return sum(1 for x in l if x == 0)

l = [-2, -1, 0, 1, 2]
print(f"Отрицательных: {cout_negative(l)}; Положительных: {count_positive(l)}; Нулевых: {count_zeros(l)}")