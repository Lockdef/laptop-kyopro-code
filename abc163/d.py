N, K = map(int, input().split())
c = 0
mod = 1000000007
for k in range(K, N + 2):
    a = k * (k - 1) / 2
    b = k * (2 * N - k + 1) / 2
    c = (c + (b - a + 1)) % mod
print(int(c))
