import math

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

ans = 0


for i in range(n):
    for j in range(i+1, n):
        x_i = s[i][0]
        y_i = s[i][1]
        x_j = s[j][0]
        y_j = s[j][1]

        ans = max(ans, math.sqrt((x_i - x_j)**2 + (y_i - y_j)**2))

print(ans)
