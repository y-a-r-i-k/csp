def main():
    n = int(input())

    sqrs = []

    i = 1
    while (i * i <= n):
        sqrs.append(i * i)
        i += 1

    return sqrs


if __name__ == "__main__":
    print(*main())