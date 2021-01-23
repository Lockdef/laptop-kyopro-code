from decimal import Decimal
n, x = map(int, input().split())
s = 0
h = Decimal(100)
for c in range(n):
    v, p = map(Decimal, input().split())
    s += v * (p / h)
    if s > x:
        print(c + 1)
        break
else:
    print(-1)
