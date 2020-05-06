N, K = map(int, input().split())
c = 0
while K <= N:
    c += 1
    N = N // K

print(c+1)
