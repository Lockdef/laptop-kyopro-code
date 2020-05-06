while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            ij = i + j + 3
            for k in range(j + 1, n):
                if k + ij == x:
                    c += 1
    print(c)
