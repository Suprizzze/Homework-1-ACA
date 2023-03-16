
def gcd(a, b, *args):
    if a == 0 or b == 0:
        print("Values must be non-zero!")
    h = list(args)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    if len(args) != 0:
        return gcd(a, h.pop(0), *h)
    return a


print(gcd(24, 36, 16, 8))

# O(n)
