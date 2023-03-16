
n = [5, 1, 2, 1, 4]
d = [i for i in n if n.count(i) >= 2]
if d:
    print(*set(d))
else:
    print(None)

# O(n) linear-time
