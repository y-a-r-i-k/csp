import math
from typing import List, Tuple

def f(x: int) -> float:
    return math.sin(x * math.pi / 8) if x <= 8 else 4 * math.cos(x * (math.pi + 1) / 5)

def calculate_seq() -> Tuple[List[float], int]:
    seq = []
    count_positive = 0
    for i in range(1, 16):
        element = f(i)
        count_positive += 1 if element > 0 else 0  
        seq.append(element)
    return seq, count_positive

def write_to_file(seq: List[float], count_positive: int) -> None:
    with open("./seq_task_15_1.bin", "wb") as file:
        for x in seq:
            file.write(format(x, '.2f').encode('utf-8') + b'\n')  
        file.write(f"{count_positive}\n".encode('utf-8'))         # Записываем кол-во положительных значений


def main():
    calculate_ = calculate_seq()
    seq, count_positive = calculate_
    write_to_file(seq, count_positive)

if __name__ == "__main__":
    main()
