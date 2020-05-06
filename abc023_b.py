n = int(input())
s = list(input())

r = ['b']

c = 0

for i in range(100):
    if r == s:
        print(c)
        break
    r.insert(0, 'a')
    r.insert(len(r), 'c')
    c += 1
    if r == s:
        print(c)
        break
    r.insert(0, 'c')
    r.insert(len(r), 'a')
    c += 1
    if r == s:
        print(c)
        break
    r.insert(0, 'b')
    r.insert(len(r), 'b')
    c += 1
else:
    print(-1)
