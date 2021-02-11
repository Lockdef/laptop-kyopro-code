x, k, d = map(int, input().split())
x = abs(x)
if k < x // d:
    print(x - k * d)
else:
    if (k - x // d) % 2 == 1:
        print(abs(x - d * (x // d + 1)))
    else:
        print(abs(x - d * (x // d)))
