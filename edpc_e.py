N, W = map(int, input().split())
weight = []
value = []
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(N):
    for sum_w in range(W + 1):
        if sum_w - weight[i] >= 0:
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i]
                                   [sum_w - weight[i]] + value[i])
        dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w])

print(dp[N][W])
