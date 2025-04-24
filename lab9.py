#variant 1 - переделать

def cnt_neg(l: list) -> int:
    cnt = 0
    for i in range(len(l)):
        if l[i] < 0:
            cnt += 1
    return cnt

def cnt_pos(l: list) -> int:
    cnt = 0
    for i in range(len(l)):
        if l[i] > 0:
            cnt += 1
    return cnt

def cnt_zer(l: list) -> int:
    cnt = 0
    for i in range(len(l)):
        if l[i] == 0:
            cnt += 1
    return cnt

l = [-2, -1, 0, 1, 2]
#print(f"Отрицательных: {cnt_neg(l)}; Положительных: {cnt_pos(l)}; Нулевых: {cnt_zer(l)}")

neg = cnt_neg(l)
pos = cnt_pos(l)
zer = cnt_zer(l)

print(neg, pos, zer)