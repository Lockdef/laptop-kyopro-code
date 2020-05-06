N, K = map(int, input().split())
P = list(map(int, input().split()))
t = [0] * 1000000
for i in range(N):
    t[i + 1] = t[i] + P[i] + 1
ans = 0
for i in range(N - K + 1):
    ans = max(ans, t[i+K] - t[i])
print(ans / 2)
