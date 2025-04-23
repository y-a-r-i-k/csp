#variant 1

import math as m

def print_ui():
    print("\tВыберете код: ")
    print("1 - y = x")
    print("2 - y = SQRT(x)")
    print("3 - y = EXP(1 / 3 * ln(x))")
    print("4 - y = SQRT(SQRT(x))")


print_ui()
choice = int(input("Ваш выбор: "))
x = int(input("x: "))
if choice == 1:
    res = x
elif choice == 2:
    res = m.sqrt(x)
elif choice == 3:
    res = m.exp(1/3 * m.ln(x))
elif choice == 4:
    res = m.sqrt(m.sqrt(x))
else:
    res = f"Опция не предусмотрена"
print(res)



#def main_v2(): #match
#    print_ui()
#    choice = int(input("Ваш выбор: "))
#    x = int(input("x: "))
#
#    match choice:
#        case 1:
#            print(x)
#            return
#        case 2:
#            print(x ** 0.5)
#            return
#        case 3:
#            print(m.exp(1/3 * m.ln(x)))
#            return
#        case 4:
#            print((x**0.5)**0.5)
#            return
#        
#    print(f"Опция ({choice}) не предусмотрена")
#        
#
#if __name__ == "__main__":
#    main_v1()
#    #main_v2()