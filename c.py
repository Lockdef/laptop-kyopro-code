n = int(input())
a = 0
b = 0
for i in range(n):
    s = []
    for j in range(int(input())):
        s.append(input().split()[1])
    if '1' in s:
        a += 1
    else:
        b += 1

print(max(a, b))
