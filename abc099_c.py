n = int(input())

dp = [10 ** 6] * (n+1)

dp[0] = 0

for i in range(n+1):
    for j in range(n):
        if i + 6 ** j > n:
            break
        dp[i + 6 ** j] = min(dp[i + 6 ** j], dp[i] + 1)
        if not i + 9 ** j > n:
            dp[i + 9 ** j] = min(dp[i + 9 ** j], dp[i] + 1)

print(dp[n])
