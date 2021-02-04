x, y, a, b = map(int, input().split())
c = 0
while x * a < x + b and x * a < y:
    x *= a
    c += 1

print(c + (y - x - 1) // b)
