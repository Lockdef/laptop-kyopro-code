W, H, N = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(N)]
area = W * H
X = [0] * W
Y = [0] * H
for x, y, a in xya:
    if a == 1:
        for i in range(x):
            X[i] = 1
    elif a == 2:
        for i in range(x, W):
            X[i] = 1
    elif a == 3:
        for i in range(y):
            Y[i] = 1
    elif a == 4:
        for i in range(y, H):
            Y[i] = 1
print(X.count(0) * Y.count(0))
