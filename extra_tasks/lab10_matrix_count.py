def main():
    n, m = map(int, input().split())
    matrix = []
    s = 0

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    target = int(input())

    for i in range(n):
        s += matrix[i].count(target)

    return s

if __name__ == "__main__":
    print(main())