from math import sqrt
n = int(input())
ans = 10000000
for a in range(1, int(sqrt(n) + 1)):
    b = n // a
    c = n % a
    ans = min(ans, abs(a - b) + c)
print(ans)
