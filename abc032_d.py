N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * W for _ in range(N)]
for i in range(N):
    for w in range(W):
        if w >= vw[i][1]:
            dp[i + 1][w] = max(dp[i][w - vw[i][1]] + vw[i][0], dp[i][w])
