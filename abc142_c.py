n = int(input())
s = [[i, j] for i, j in zip(map(int, input().split()), range(1, n+1))]
s = sorted(s, key=lambda x: x[0])
for i in range(n):
    print(s[i][1], end=" ")
print()
