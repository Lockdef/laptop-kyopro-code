n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [a[0] * b[0]]
ma = a[0]
for i in range(1, n):
    ma = max(ma, a[i])
    c.append(max(c[i - 1], ma * b[i]))
for i in c:
    print(i)
