n, k = map(int, input().split())
h = list(map(int, input().split()))
h = sorted(h, reverse=True)
if n <= k:
    print(0)
else:
    print(sum(h[k:]))
