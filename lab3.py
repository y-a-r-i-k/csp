import math


def side_len(R, n) -> float:
    return 2 * R * math.sin(math.pi / n)

def calculate_r(R, n) -> float:
    return R * math.cos(math.pi / n)

def polygon_area(R, n) -> float:
    return (0.5 * n * side_len(R, n) * calculate_r(R, n))

def circle_area(R) -> float:
    return (math.pi * (R ** 2))

    
R = int(input())
print(f"{polygon_area(R, 10)}\t{circle_area(R)}")
print(f"{polygon_area(R, 50)}\t{circle_area(R)}")
print(f"{polygon_area(R, 100)}\t{circle_area(R)}")

