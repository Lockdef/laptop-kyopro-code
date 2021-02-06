from collections import deque, defaultdict
n, m = map(int, input().split())
g = [defaultdict(int) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a - 1][b - 1] = c
dp = [[float("inf") for _ in range(n)] for _ in range(n)]
for start in range(n):
