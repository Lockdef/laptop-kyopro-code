N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(M):
    for j in range(i + 1, M):
        c = 0
        for a in A:
            c += max(a[i], a[j])
        ans = max(ans, c)
print(ans)
