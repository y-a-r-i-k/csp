def main():
    original = list(map(int, input().split()))
    result = []

    for i in range(len(original)):
        if (original[i] % 2 == 0):
            result.append(original[i])

    return result


if __name__ == "__main__":
    print(*main())