from collections import Counter
n = int(input())
a = list(map(int, input().split()))
ca = Counter(a)
sa = sum(a)
q = int(input())
for _ in range(q):
    b, c = map(int, input().split())
    sa += (c - b) * ca[b]
    ca[c] += ca[b]
    ca[b] = 0
    print(sa)
