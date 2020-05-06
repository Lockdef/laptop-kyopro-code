N = int(input())
a = list(map(int, input().split()))

if sum(a) % N:
    print(-1)
else:
    s = sum(a) // N
    c = 0
    t = 0
    for i in range(N):
        c += a[i] - s
        if c:
            t += 1
    print(t)
