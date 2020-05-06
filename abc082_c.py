from collections import Counter
N = int(input())
a = list(map(int,input().split()))
c = Counter(a)
ans = 0
for i, j in c.items():
    if i <= j:
        ans += j - i
    else:
        ans += j
print(ans)
