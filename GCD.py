
def gcd(a, b, *args):
    if a == 0 and b == 0:
        return "Values must be non-zero!"
    h = list(args)
    if a == 0 and b == 0 and args is None:
        return a + b
    while a != 0 and b != 0:
        a, b = b, a % b
    if len(args) != 0:
        if a != 0:
            return gcd(a, h.pop(0), *h)
        if b != 0:
            return gcd(b, h.pop(0), *h)
    return a


print(gcd(24, 36, 16))


# O(n)
