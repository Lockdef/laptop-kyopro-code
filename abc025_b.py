n, a, b = map(int, input().split())
sd = [input().split() for _ in range(n)]
c = 0

for i in sd:
    s = i[0]
    d = int(i[1])
    if s == "East":
        e = -1
    else:
        e = 1
    if d < a:
        c += a * e
    elif d > b:
        c += b * e
    else:
        c += d * e

if c < 0:
    print("East", -1 * c)
elif c == 0:
    print(0)
else:
    print("West", c)
