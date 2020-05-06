from math import ceil
h, n = map(int, input().split())
s = [list(map(int, input().split())) for _ in [0] * n]

a = sorted(s, key=lambda x: x[0] / x[1])[-1]

b = (h // a[0]) * a[1]
print(a, b)
c = h % a[0]
print(c)
d = 0
if c != 0:

    d = 10000000000

    for i in range(n):
        print(s[i], d, ceil(c / s[i][0]))
        d = min(d, s[i][1] * ceil(c / s[i][0]))
print(d)
print(b + d)
