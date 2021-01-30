n, m = map(int, input().split())
ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
x = [0 for _ in range(n)]  # 皿のボール数
count = [0 for _ in range(n)]
for i in cd:
    count[i[0]] += 1
    count[i[1]] += 1
for i in cd:
    c = i[0]
    d = i[1]
    if count[c] <= count[d] and x[c] != 1:
        x[c] += 1
    else:
        x[d] += 1
    count[c] -= 1
    count[d] -= 1
r = 0
for i in ab:
    a = i[0]
    b = i[1]
    if x[a] > 0 and x[b] > 0:
        r += 1
print(r)
