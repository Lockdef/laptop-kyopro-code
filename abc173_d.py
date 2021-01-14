from math import ceil
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
res = a[0]
for i in range(1, n - 1):
    res += a[ceil(i / 2)]
print(res)
