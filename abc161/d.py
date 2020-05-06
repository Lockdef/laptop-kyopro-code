o = int(input())
c = -1
for i in range(1000000000000):
    i = str(i)
    t = 0
    for j in range(len(i)):
        k = abs(int(i[j - 1]) - int(i[j]))
        if k > 1:
            t = 1
            break
    if t:
        continue
    c += 1
    if c == o:
        print(i)
        break
