N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]
S = [1] + [0] * (N-1)
sc = sorted(sc, key=lambda x: x[0])


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


if N != 1 and [1, 0] in sc:
    print(-1)
elif len(list(set([i[0] for i in sc]))) != len(list(get_unique_list(sc))):
    print(-1)
elif N == 1 and M == 0:
    print(0)
else:
    for i in sc:
        S[i[0]-1] = "{}".format(i[1])

    print(*S, sep="")
