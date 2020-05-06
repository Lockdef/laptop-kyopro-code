N, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in [0] * N]
value = [s[0] for s in S]
weight = [s[1] for s in S]
dp = [[0] * (W + 1) for i in range(N + 1)]

for i in range(N):
    for w in range(W + 1):
        if (w >= weight[i]):
            dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            # print(dp[i+1][w], value[i])
            # print(f"{dp[i][w-weight[i]]} + {value[i]}")
        else:
            dp[i + 1][w] = dp[i][w]

print(dp[N][W])
