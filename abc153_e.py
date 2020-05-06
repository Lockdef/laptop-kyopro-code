H, N = map(int, input().split())
S = [list(map(int, input().split())) for _ in [0] * n]
dp = [[float("-inf")] * (H + 1)] * N
for i in range(W+1):
    dp[0][i] = 0

for i in range(N):
    for h in range(H+1):
        if S[i][0]
