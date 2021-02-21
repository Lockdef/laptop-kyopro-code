x = input()
m = int(input())
d = max(map(int, x))


def base(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n**(i - 1))
    return out


c = 0
for i in range(d + 1, 100000000000000000):
    a = base(str(x), i)
    print(a, i)
    if a <= m:
        c += 1
    else:
        break
print(c)
