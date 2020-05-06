L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

c = 0
for i in l:
    if i in r:
        c += 1
        r.pop(r.index(i))

print(c)
