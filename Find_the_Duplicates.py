n = [5, 1, 2, 1, 4]
z = set(n)

result = list(filter(lambda x: n.remove(x) in n, z))
if len(n) == 0:
    print(None)
else:
    print(*set(n))