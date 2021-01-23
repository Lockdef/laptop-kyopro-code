n = int(input())
a = list(map(int, input().split()))
s = -1
for l in range(n):
    m = a[l]
    for r in range(l, n):
        m = min(m, a[r])
        s = max(s, m * (r - l + 1))
print(s)
