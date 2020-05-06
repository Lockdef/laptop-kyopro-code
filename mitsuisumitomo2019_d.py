N = int(input())
S = input()
t = ["{:03d}".format(i) for i in range(0, 1000)]

c = 0
for i in t:
    a = 0
    b = 0
    if S.count(i[0]):
        a = S.index(i[0])
        if S[a + 1:].count(i[1]):
            b = S[a + 1:].index(i[1]) + a + 1
            if S[b + 1:].count(i[2]):
                c += 1

print(c)
