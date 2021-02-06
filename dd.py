from math import ceil, floor, sqrt
x, y, r = map(float, input().split())
num = 0
start = ceil(x - r)
end = floor(x + r)
for i in range(start, end + 1):
    p = sqrt(pow(r, 2) - pow(x - i, 2))
    bottom = ceil(y - p)
    top = floor(y + p)
    num += top - bottom + 1
print(num)
