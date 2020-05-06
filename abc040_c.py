N = int(input())
a = list(map(int, input().split()))
dp = [float("inf") for _ in range(1000000)]
dp[0] = 0
for i in range(N):
    for j in range(1, 3):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(a[i] - a[i + j]))
print(dp[N - 1])
