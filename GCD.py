
def gcd(a, b, *args):
    if a == 0 or b == 0:
        raise ValueError("Values must be non-zero!")
    h = list(args)
    while a != 0 and b != 0:
        a, b = b, a % b
    if len(args) > 0:
        if a != 0:
            return gcd(a, h.pop(0), *h)
        return gcd(b, h.pop(0), *h)
    return a


print(gcd(16, 36, 24))


# O(n)
