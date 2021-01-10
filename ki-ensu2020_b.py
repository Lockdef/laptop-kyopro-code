n = int(input())
x = []
for _ in range(n):
    x_, l_ = map(int, input().split())
    x.append([x_ - l_, x_ + l_])
x.sort(key=lambda x: x[1])
c = 1
for i in range(n - 1):
    r = x[i][1]
    l = x[i + 1][0]
    if r <= l:
        c += 1
    else:
        x[i + 1][1] = r
print(c)
