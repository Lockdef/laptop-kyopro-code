N = int(input())
h = list(map(int, input().split()))
dp = [1000000] * N
dp[0] = 0
for i in range(N):
    for j in range(1, 3):
        if i + j < N:
            dp[i + j] = min(dp[i] + abs(h[i] - h[i + j]), dp[i + j])

print(dp[-1])
