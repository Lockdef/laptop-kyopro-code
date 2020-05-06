n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sum(a) / (4 * m)
c = 0
for i in a:
    if i >= b:
        c += 1
if c >= m:
    print("Yes")
else:
    print("No")
