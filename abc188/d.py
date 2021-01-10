n, c = map(int, input().split())
abc = [list(map(abc, input().split())) for _ in range(n)]
last = max([abc[i][1] for i in range(n)])
r = []
all_cost = sum([abc[i][2] for i in range(n)])
if all


def isBetween(x, i):
    global abc
    return abc[i][0] <= x <= abc[i][1]
