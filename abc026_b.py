import math
N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=True)
S = 0
PI = math.pi
for i in range(N):
    if i == 0:
        S += R[0] ** 2 * PI
    elif i % 2:
        S -= R[i] ** 2 * PI
    else:
        S += R[i] ** 2 * PI
print(S)
