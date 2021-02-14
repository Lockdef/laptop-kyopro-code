n = int(input())
b = list(map(lambda x: int(x) - 1, input().split()))
r = []
while b:
    t = -1
    for i in range(len(b)):
        if i == b[i]:
            t = i
    if t == -1:
        print(-1)
        exit()
    r.append(t)
    b.pop(t)
for i in r[::-1]:
    print(i + 1)
