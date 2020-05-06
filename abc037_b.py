N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]
ans = [0] * N
for l, r, t in LRT:
    for i in range(l - 1, r):
        ans[i] = t
for i in ans:
    print(i)
