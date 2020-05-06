a, b, k = map(int, input().split())
if k > a:
    k -= a
    a = 0
    b -= k
    if b < 0:
        b = 0
elif k <= a:
    a -= k

print(a, b)
