def main():
    n = int(input())

    i = 2
    while n==n:
        if (n % i == 0):
            return i
        i += 1

if __name__ == "__main__":
    print(main())