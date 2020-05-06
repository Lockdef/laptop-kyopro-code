from itertools import combinations
n, k = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in combinations(a, 3):
    if sum(i) == k:
        c += 1
print(c)
