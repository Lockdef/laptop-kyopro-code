n = int(input())
a = list(map(int, input().split()))
c = a

while len(a) != 2:
    n = len(a) // 2
    b = []
    for i in range(1, n + 1):
        b.append(max(a[2*i - 2], a[2*i - 1]))
    a = b

print(c.index(min(a)) + 1)
