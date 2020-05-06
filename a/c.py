
h, w, k = map(int, input().split())
s = []
for i in range(h):
    s.append(input().split())

r = []

for i in range(h):
    r.append([])

# 各行にいちごが含まれているかの2値リスト
kl = []

for i in range(h):
    if('#' in s[i]):
        kl.append(0)
    else:
        kl.append(1)

# いちごが含まれている行に一度でもあたったか判定
isk = True

count = 1


for i in range(h):
    if isk and kl[i] == 0:
        continue
    for j in range(w):
        if(s[i][0][j] == '.'):
            r[i].append(count)
        elif(s[i][0][j] == '#'):
            r[i].append(count)
            count += 1
    if isk:
        if kl[i] == 1:
            isk = False
            for n in range(i):
                r[n].append(h[i])

for i in r:
    print(*i)
