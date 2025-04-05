#variant 1

def main():
    s = 0 #sum
    for i in range(11):
        s += (1.2**(4*i + 1)) / (4*i + 1)

    print(s)

if __name__ == "__main__":
    main()