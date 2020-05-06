n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(2 * n)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abc[i][k])

print(max(dp[n]))
