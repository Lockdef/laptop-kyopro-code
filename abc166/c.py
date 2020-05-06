N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
ways = [[] for _ in range(N)]
for ab in AB:
    ways[ab[0] - 1].append(ab[1] - 1)
    ways[ab[1] - 1].append(ab[0] - 1)
c = 0
for i in range(N):
    if len(ways[i]) == 0:
        c += 1
        continue
    t = 0
    for j in ways[i]:
        if H[i] <= H[j]:
            break
    else:
        c += 1
print(c)
