#variant 1

import math

def f(x):
    return 2 * math.sin(3/4 * x)

def find_closest_point(start, end, step):
    min_distance_squared = float('inf')
    closest_point = (0, 0)

    x = start
    while x <= end:
        y = f(x)
        distance_squared = x**2 + y**2
        
        if distance_squared < min_distance_squared:
            min_distance_squared = distance_squared
            closest_point = (x, y)
        
        x += step

    return closest_point

start = 0.1  
end = 10
step = 0.1

closest_point = find_closest_point(start, end, step)
print(f"Координаты ближайшей точки: {closest_point}")
