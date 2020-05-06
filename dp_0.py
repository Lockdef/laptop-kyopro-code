n = int(input())
a = list(map(int, input().split()))

dp = 0

for i in range(n):
    dp = max(dp, dp + a[i])

print(dp)
