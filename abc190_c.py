n, m = map(int, input().split())
ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
mc = 0
for bit in range(2 ** k):
    s = [0 for _ in range(n)]
    for i in range(k):
        if bit & (1 << i):
            s[cd[i][0]] += 1
        else:
            s[cd[i][1]] += 1
    c = 0
    for i in ab:
        if s[i[0]] > 0 and s[i[1]] > 0:
            c += 1
    mc = max(mc, c)
print(mc)
