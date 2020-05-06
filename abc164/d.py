S = input()
t = []
for i in range(1, 1000):
    t.append(str(2019 * i))
c = 0
for i in t:
    if S.count(i):
        a = len(i)
        for j in range(len(S) - a + 1):
            if S[j:j + a] == i:
                c += 1

print(c)
