N = int(input())
A = list(map(int, input().split()))
l = [0] * 10000001
for i in A:
    l[i] += 1
s = 0
for i in range(N + 1):
    i = l[i]
    s += i * (i - 1) // 2
for a in A:
    a = l[a]
    print(s - (a * (a - 1) // 2) + ((a - 1) * (a - 2) // 2))
