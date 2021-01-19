from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(n + 1)
a.append(0)
a.sort()
d = []
md = n
for i in range(m + 1):
    d_ = a[i + 1] - a[i] - 1
    d.append(d_)
    if d_ == 0:
        continue
    md = min(md, d_)
c = 0
for i in d:
    c += ceil((i) / md)
print(c)
