N = int(input())
a = list(map(int, input().split()))

s = float("inf")
for i in range(min(a), max(a) + 1):
    t = 0
    for j in a:
        t += (j - i) ** 2
    s = min(s, t)
print(s)
