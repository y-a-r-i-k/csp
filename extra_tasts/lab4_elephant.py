#К задаче неправильный тест

#Нормальный тест:
#Input: 1 1 3 2
#Output: Yes

def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        return 'YES'
    else:
        return 'NO'
    

if __name__ == "__main__":
    print(main())