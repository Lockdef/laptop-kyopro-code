from math import ceil

n, h = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

a = [i[0] for i in s]
b = [i[1] for i in s if max(a) < i[1]]

c = 0

for i in b:
    h -= i
    c += 1
    if h <= 0:
        print(c)
        exit()

print(ceil(h/max(a)) + c)
