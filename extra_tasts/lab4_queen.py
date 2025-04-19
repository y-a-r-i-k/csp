def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    
    if (x1 - x2) * (y1 - y2) == 0 or abs(x1 - x2) == abs(y1 - y2):
        return 'YES'
    else:
        return 'NO'
    

if __name__ == "__main__":
    print(main())