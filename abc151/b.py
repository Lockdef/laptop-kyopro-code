n, k, m = map(int, input().split())
a = list(map(int, input().split()))

c = m*n
if sum(a)+k < c:
    print(-1)
else:
    if c - sum(a) > -1:
        print(c - sum(a))
    else:
        print(0)
