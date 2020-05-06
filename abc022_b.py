from collections import Counter

n = int(input())
a = [int(input()) for _ in range(n)]

c = Counter(a)

s = 0

for i in c:
    if c[i] > 1:
        s += c[i] - 1

print(s)
