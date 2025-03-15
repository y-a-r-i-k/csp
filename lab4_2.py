def mymax(a, b):
    return a if a > b else b

def main():
    x1, x2, x3, x4 = map(int, input().split())
    print(mymax(mymax(x1, x2), mymax(x3, x4)))


if __name__ == "__main__":
    main()