from itertools import permutations
from math import sqrt
N = int(input())
S = [list(map(int, input().split())) for _ in [0] * N]
t = []
for i in permutations(list(range(N))):
    for j in range(N-1):
        t.append(sqrt((S[i[j]][0] - S[i[j+1]][0]) **
                      2 + (S[i[j]][1] - S[i[j+1]][1]) ** 2))
print(sum(t) / len(t))
