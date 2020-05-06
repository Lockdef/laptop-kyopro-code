n, t = map(int, input().split())
a = [int(input()) for _ in [0] * n]

s = 0

for i in range(n-1):
    if a[i+1] - a[i] < t:
        s += a[i+1] - a[i]
    else:
        s += t
else:
    s += t

print(s)
