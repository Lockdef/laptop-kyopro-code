A, B, N = map(int, input().split())
c = 0
t = -10
if N > 100000000:
    for i in range(100000000, N + 1):
        a = (i * A) // B - A * (i // B)
        c = max(c, a)
        if t > a or i > 200000000:
            print(c)
            break
        t = a
    else:
        print(c)
else:
    for i in range(N + 1):
        a = (i * A) // B - A * (i // B)
        c = max(c, a)
        if t > a or i > 100000000:
            print(c)
            break
        t = a
    else:
        print(c)
