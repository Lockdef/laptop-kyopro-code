a, b, c, d = map(int, input().split())

x = [i for i in range(a, b)]
y = [i for i in range(c, d)]
s = 0
for i in x:
    if i in y:
        s += 1
print(s)
