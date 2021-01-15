n = int(input())
a = list(map(int, input().split()))
a.sort()
r = 0
sum_a = 0
for i in range(n):
    r += i * a[i] - sum_a
    sum_a += a[i]
print(r)
