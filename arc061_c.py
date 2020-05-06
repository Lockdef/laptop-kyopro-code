s = input()

ans = 0

n = len(s)-1

for i in range(2 ** n):
    bag = []
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(1)
        else:
            bag.append(0)
    c = 0

    temp = s
    for j in range(0, n):
        c += 1
        if (bag[j]):
            temp = temp[:c] + '+' + temp[c:]
            c += 1

    ans += eval(temp)


print(ans)
