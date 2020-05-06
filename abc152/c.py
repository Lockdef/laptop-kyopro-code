n = int(input())
p = list(map(int, input().split()))
t = n
c = 0
for i in range(n):
    t = min(t, p[i])
    if p[i] <= t:
        c += 1
print(c)
