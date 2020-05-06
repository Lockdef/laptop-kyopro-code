n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in [0] * n]

s = 0

for i in range(n):
    for j in range(m):
        t = []
        for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            i_ = i
            j_ = j
            if 0 > x or 0 > y:
                continue
            k = a[i][j] - a[i + y][j + x]
            if -1 < k:
                t.append(a[i][j] - a[i + y][j + x])
