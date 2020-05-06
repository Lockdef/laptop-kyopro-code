from math import factorial
n, a, b = map(int, input().split())


def cc(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


mod = 10 ** 9 + 7
s = (2 ** n - 1) % mod

s -= (cc(n, a) + cc(n, b)) % mod

print(s)
