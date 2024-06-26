# Newton's Method

s = lambda r: sum((900-3*k) * (r**(k-1)) for k in range(1, 5001)) + 6e11

ds = lambda r: sum((900-3*k) * (k-1) * r**(k-2) for k in range(1, 5001))

x = 1.1
for i in range(1000):
    x -= s(x) / ds(x)
    print(x, s(x))

print(round(x, 12))