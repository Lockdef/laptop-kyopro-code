n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h = sorted(h, reverse=True)
t = []
for i in range(n - k + 1):
    t.append(h[i] - h[i + k - 1])

print(min(t))
