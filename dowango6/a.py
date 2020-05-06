n = int(input())
s = [input().split() for _ in range(n)]
x = input()

t = False

c = 0

for i in s:
    if t:
        c += int(i[1])
    if i[0] == x:
        t = True

print(c)
