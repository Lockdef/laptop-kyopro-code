N, X, Y = map(int, input().split())
X -= 1
Y -= 1
ans = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        c = min(j - i, abs(X - i) + abs(Y - j) + 1)
        ans[c] += 1
for i in ans[1:]:
    print(i)
