#variant 1
def f(x):
    if -2 <= x <= -1:
        return 2 * x + 4
    if -1 < x <= 1:
        return 2 * (x ** 2)
    if 1 < x <= 2:
        return -2 * x + 2
    if x < -2 or x > 2:
        return None #Undef function

def main():
    print(f(int(input())))


if __name__ == "__main__":
    main()