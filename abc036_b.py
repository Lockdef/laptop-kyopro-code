N = int(input())
s = [input() for _ in range(N)]

for i in range(N):
    t = []
    for j in range(N):
        t.append(s[j][i])
    print(*t[::-1], sep="")
