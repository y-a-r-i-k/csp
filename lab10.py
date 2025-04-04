#variant 1

#Задаем произвольную матрицу:

b = [[1, 2, 3], [3, 2, 1], [4, 5, 4]] #Задаем вручную
a = [[0] * 3] * 3

def min_in_matrix(m: list[list]) -> int:
    min_val = float('inf')
    for i in range(len(m)):
        inner_min = min(m[i])
        
        if min_val > inner_min:
            min_val = inner_min
    return min_val

def max_in_matrix(m: list[list]) -> int:
    max_val = -float('inf')
    for i in range(len(m)):
        inner_max = max(m[i])
        
        if max_val < inner_max:
            max_val = inner_max
    return max_val

b_max_element = max_in_matrix(b)
b_min_element = min_in_matrix(b)

for i in range(len(b)):
    for j in range(len(b[i])):
        a[i][j] = (2 * b[i][j] + b_min_element) / b_max_element

print(a)