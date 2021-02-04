from functools import reduce
from math import gcd

n = int(input())
t = [int(input()) for _ in range(n)]
print(reduce(lambda x, y: (x * y) // gcd(x, y), t, 1))
