N, M = map(int, input().split())
c = 0
l = [*list(range(2, 2*N+1, 2)), *list(range(1, M*2, 2))]
for i in l:
    for j in l:
        if i == j:
            continue
        k = i + j
        if k % 2:
            pass
        else:
            c += 1

print(c // 2)
