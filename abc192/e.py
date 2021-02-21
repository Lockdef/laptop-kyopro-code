from collections import deque
n, m, x, y = map(int, input().split())
x -= 1
y -= 1
g = [{} for _ in range(n)]  # 各駅から行ける駅
for i in range(m):
    a, b, t, k = map(int, input().split())
    g[a - 1][b - 1] = [t, k, i]
    g[b - 1][a - 1] = [t, k, i]
e = [True for _ in range(m)]
dp = [float("inf") for _ in range(n)]
dp[x] = 0
que = deque([x])
for _ in range(100000000):
    if not que:
        break
    i = que.pop()
    for a, b in g[i].items():  # a: 行き先 b: [かかる時間, 倍数]
        if not e[b[2]]:
            continue
        e[b[2]] = False
        if dp[i] % b[1] == 0:
            dp[a] = min(dp[a], dp[i] + b[0])
        else:
            dp[a] = min(dp[a], dp[i] + b[0] + b[1] - dp[i] % b[1])
        que.append(a)


if dp[y] == float("inf"):
    print(-1)
else:
    print(dp[y])
