n, a, b = map(int, input().split())


if (b - a) % 2 == 0:
    print(min(b - 1, n - a, (b - a) // 2))
else:
    print(min(b - 1, n - a))
