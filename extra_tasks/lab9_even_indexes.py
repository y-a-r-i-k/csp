def main():
    original = list(map(int, input().split()))
    result = []

    for i in range(0, len(original), 2):
        result.append(original[i])
        
    return result


if __name__ == "__main__":
    print(*main())