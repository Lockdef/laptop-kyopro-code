a, b = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(lambda x: bool(int(x)), bin(b)[2:]))[::-1]
t = 0

for i in range(len(b)):
    if b[i]:
        t += s[i]
print(t)
