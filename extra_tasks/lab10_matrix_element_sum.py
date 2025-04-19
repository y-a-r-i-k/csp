def main():
    n, m = map(int, input().split())
    s = 0

    for _ in range(m):
        s += sum(list(map(int, input().split())))

    return s
    

if __name__ == "__main__":
    print(main())