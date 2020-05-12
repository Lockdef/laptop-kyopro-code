N, K = map(int,input().split())
A = list(map(lambda x: int(x) - 1,input().split()))
seen = [0] * N
seen[0] = 1
a = 0
i = A[0]
while True:
    if seen[i]:
        b = A[i]
        a += 1
        break
    seen[i] = 1
    a += 1
    i = A[i]
c = 0
i = A[0]
while True:
    if i == b:
        c += 1
        break
    c += 1
    i = A[i]
d = a - c + 1
is_heiro = False
e = []
i = A[0]
while True:
    if i == b and is_heiro:
        break
    if i == b:
        is_heiro = True
    if is_heiro:
        e.append(i)
    i = A[i]
if K <= a:
    i = A[0]
    for _ in range(K - 1):
        i = A[i]
    print(i + 1)
else:
    a = ((K + 2) - (a - d)) % d
    print(e[a] + 1)
