n, y = map(int, input().split())

c = y // 10000 + (y % 10000) // 5000 + (y % 5000) // 1000

if c <= n:
    print(y // 10000, (y % 10000) // 5000, (y % 5000) // 1000)
else:
    print(-1, -1, -1)
