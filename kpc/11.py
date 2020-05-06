m, n, N = map(int, input().split())
c = 0
while N != 0:
    print(N)
    c += N
    N = n * (N // m)

print(c)
