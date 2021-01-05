from itertools import combinations as c

n, m = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(m)]

max_count = 0

for bit in range(2 ** n):
    p = []
    isFaction = True
    count = 0
    for i in range(n):
        if bit & (1 << i):
            p.append(i + 1)
            count += 1
    for pair in c(p, 2):
        if not (pair in xy or pair[::-1] in xy):
            isFaction = False
    if isFaction:
        max_count = max(max_count, count)

print(max_count)
