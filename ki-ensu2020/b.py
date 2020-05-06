n = int(input())
s = [list(map(int, input().split())) for _ in [0] * n]

s = sorted(s, key=lambda x: x[0])

c = 0
for i in range(10):
    i = 0
    while (i != len(s)-1 and i < len(s)):
        if s[i][1] >= abs(s[i][0] - s[i+1][0]):
            c += 1
            s.pop(i)
        i += 1


print(n-c)
