import math
A, B, N, M = map(int, input().split())
a = (N * 60 + M) / 2
b = M * 6
c = abs(a - b)
c = math.radians(min(c, 360 - c))
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(c)))
