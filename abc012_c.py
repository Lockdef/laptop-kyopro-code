N = int(input())
c = 0
t = [[] for _ in range(100)]
for i in range(1, 10):
    for j in range(1, 10):
        a = i * j
        c += a
        t[a] += ["{} x {}".format(i, j)]
for i in t[c - N]:
    print(i)
