#nok

def lcm(a: int, b: int) -> int:
    n = min(a, b)
    while True:
        if n%a==0 and n%b==0:
            break
        n += 1
    return n