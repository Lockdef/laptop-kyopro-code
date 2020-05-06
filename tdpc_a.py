N = int(input())
p = list(map(int, input().split()))
dp = [[False] * (100 * 101) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j, dpj in enumerate(dp[i - 1]):
        if dpj:
            dp[i][j] = True
            dp[i][j + p[i]] = True
ans = 0
for dpi in dp[N - 1]:
    if dpi is True:
        ans += 1
print(ans)
