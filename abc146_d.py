n = int(input())
s = [list(map(int, input().split())) for _ in [0] * (n-1)]

a = [0] * n


for i in s:
    a[i[0]-1] += 1
    a[i[1]-1] += 1

print(max(a))

b = [0] * n

c = [[]] * n

for i in s:
    b[i[0]-1] += 1
    b[i[1]-1] += 1
    if max(b[i[0]-1], b[i[1]-1]) in c[i[0]-1] or max(b[i[0]-1], b[i[1]-1]) in c[i[1]-1]:
        d = []
        d += c[i[0]-1]
        d += c[i[1]-1]
        d = set(d)
        print(set(d))
        e = [i for i in range(max(a))]
        f = [i for i in e if i not in d]
        print(f[0])
    else:
        print(max(b[i[0]-1], b[i[1]-1]))
    c[i[0]-1] += [max(b[i[0]-1], b[i[1]-1])]
    c[i[1]-1] += [max(b[i[0]-1], b[i[1]-1])]
    print(i[0], i[1], ":", c)
