import math

class Polygon:
    def __init__(self, R, n) -> None:
        self.R = R  # Radius
        self.n = n  # number of sides

    def side_len(self) -> float:
        return 2 * self.R * math.sin(math.pi / self.n)
    
    def calculate_r(self) -> float:
        return self.R * math.cos(math.pi / self.n)
    
    def polygon_area(self) -> float:
        return (0.5 * self.n * self.side_len() * self.calculate_r())
    
    def circle_area(self) -> float:
        return (math.pi * (self.R ** 2))
    
    
def main():
    R = int(input())
    polygon10 = Polygon(R, 10)
    polygon50 = Polygon(R, 50)
    polygon100 = Polygon(R, 100)

    print("Polygon Area | Circle Area")
    print(f"{polygon10.polygon_area():.2f} | {polygon10.circle_area():.2f}")
    print(f"{polygon50.polygon_area():.2f} | {polygon50.circle_area():.2f}")
    print(f"{polygon100.polygon_area():.2f} | {polygon100.circle_area():.2f}")

if __name__ == "__main__":
    main()
