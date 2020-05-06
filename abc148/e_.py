n = int(input())

if n % 2 == 0:
    x = n // 10 + n // 50

    m = len(str(n))

    if m > 2:
        for i in range(1, m - 1):
            x += n // (25 * (10 ** i))
    if m > 3:
        for i in range(1, m - 2):
            print((125 * (10 ** i)))
            x += n // (125 * (10 ** i))
    print(x)
else:
    print(-1)
