N = int(input())
num = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        for n in range(N + 1):
            n = str(n)
            if str(i + 1) == n[0] and str(j + 1) == n[-1]:
                num[i][j] += 1
s = 0
for i in range(9):
    for j in range(9):
        s += num[i][j] * num[j][i]
print(s)
