#v1

import random as rnd
import re


def mode_1(n: int): #Запись в файл
    try:
        f = open("Data.txt", "w")
    except FileNotFoundError:
        print("[ERROR] Файл не найден")
    
    content = []
    alf = 'XYZ1234567890'

    for _ in range(n):
        content.append("".join([rnd.choice(alf) for __ in range(rnd.randrange(10, 100))]) + "\n")

    f.writelines(content)
    f.close()


def mode_2(): #Обработака содержимого
    try:
        f = open("Data.txt", "r")
    except FileNotFoundError:
        print("[ERROR] Файл не найден")

    max_number = -1
    max_number_index = 0
    lines = f.readlines()
    for line, index in zip(lines, range(len(lines))):
        line_numbers = re.split(r'\D', line)
        in_line_max = max([int(x) if x != "" else 0 for x in line_numbers])
        if (in_line_max > max_number):
            max_number = in_line_max
            max_number_index = index

    max_number_line = lines[max_number_index]
    y_count = max(re.split(r"[^Y]*", max_number_line))

    print(f"{max_number_index, max_number, y_count}")

def main():
    s = int(input("Выберете режим: "))
    if s == 1:
        n = int(input("Введите кол-во строк: "))
        mode_1(n)
    elif s == 2:
        mode_2()
    else: 
        print("Такой режим не предусмотрен")

if __name__ == "__main__":
    main()