n, m = map(int, input().split())
x = sorted(set(map(int, input().split())))
t = []
for i, j in zip(x, x[1:]):
    t += [abs(i - j)]
t = sorted(t, reverse=True)
print(sum(t[n-1:]))
