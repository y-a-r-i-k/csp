def y(a: float) -> float:
    p = 1
    for i in range(10, 0, -1):
        n = i**2 + a**2
        d = i * (i + a)
        p *= d / n

    s = 0
    for k in range(4, 1, -1):
        a1 = a ** (k + 1)
        s += k**3 / (k + a1)
    return (a**3 / 2) * p + s

def main(a0, ah, an):
    s = 0
    a = a0
    print(f"a\ty(a)")
    while a <= an:
        s += y(a)
        print(f"{a}\t{y(a):.4f}")
        a += ah
    print(s)


if __name__ == "__main__":
    a0 = int(input())
    ah = int(input())
    an = int(input())
    main(a0, ah, an)