N = int(input())
A, x, y = [], [], []
for i in range(N):
    A.append(int(input()))
    x_, y_ = [], []
    for j in range(A[i]):
        x__, y__ = map(int, input().split())
        x_.append(x__ - 1)
        y_.append(y__)
    x.append(x_)
    y.append(y_)
ans = 0
for i in range(2 ** N):
    t = 1
    for j in range(N):
        if not i & (1 << j):
            continue
        for a, b in zip(x[j], y[j]):
            if b == 1 and not i & (1 << a):
                t = 0
                break
            if b == 0 and i & (1 << a):
                t = 0
                break
        if not t:
            break
    if t:
        ans = max(ans, bin(i).count("1"))
print(ans)
