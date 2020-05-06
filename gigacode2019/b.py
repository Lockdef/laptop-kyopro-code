n, x, y, z = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

c = 0

for i in range(n):
    a = s[i][0]
    b = s[i][1]
    if (x <= a and y <= b and z <= (a + b)):
        c += 1

print(c)
