N, M, X = map(int,input().split())
ca = [list(map(int,input().split())) for _ in range(N)]

s = float('inf')

for i in range(2 ** N):
    rikai = [0] * M
    total = 0
    is_rikai = True
    for j in range(N):
        if ((i >> j) & 1):
            total += (ca[j][0])
            for k in range(1, M + 1):
                rikai[k - 1] += ca[j][k]
    for l in rikai:
        if l < X:
            is_rikai = False
    if is_rikai:
        s = min(s, total)

if s == float('inf'):
    print(-1)
else:
    print(s)
