def main():
    a, b, c, d = map(int, input().split())

    numbers = []
    for i in range(a, b + 1):
        if (i % d == c):
            numbers.append(i)
    return numbers 



if __name__ == "__main__":
    print(*main())