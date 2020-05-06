d = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

temp = 0

s = []

for i in range(d):
    temp += a[i]
    if (b[i] < temp):
        s.append(b[i])

if len(s) != 0:
    print(min(s))
else:
    print('-1')
