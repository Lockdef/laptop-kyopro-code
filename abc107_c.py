N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = 10000000000000000000000

for i in range(N - K):
    ans = min(ans, abs(x[i] + abs(x[i + K] - x[i])))

print(ans)
