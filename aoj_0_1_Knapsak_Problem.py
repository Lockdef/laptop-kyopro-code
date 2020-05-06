N, W = map(int, input().split())
value = []
weight = []
for i in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(N):
    for max_w in range(W + 1):
        if max_w >= weight[i]:
            dp[i + 1][max_w] = max(dp[i][max_w],
                                   dp[i][max_w - weight[i]] + value[i])
        else:
            dp[i + 1][max_w] = dp[i][max_w]
print(dp[N][W])
