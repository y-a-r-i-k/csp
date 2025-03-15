#variant 1

def main():
    n = int(input("Сколько элементов вывести?: "))
    
    for i in range(1, n + 1):
        print(f"a{i}={1/(i**2)}")

if __name__ == "__main__":
    main()