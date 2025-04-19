def main():
    a, b = map(int, input().split())

    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

if __name__ == "__main__":
    print(*main())