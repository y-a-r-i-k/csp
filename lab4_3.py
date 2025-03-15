#variant 1

def check(x, y, r_in, r_out, x1, y1) -> bool:
    if ((x - x1) ** 2 + (y - y1) ** 2 >= r_in ** 2) and ((x - x1) ** 2 + (y - y1) ** 2 <= r_out ** 2):
        return True
    return False
    

def main():
    x, y = map(int, input("(x, y): ").split())
    r_in, r_out = map(int, input("(r, R): ").split())
    x1, y1 = map(int, input("(x1, y1): ").split())

    print(check(x, y, r_in, r_out, x1, y1))

if __name__ == "__main__":
    main()