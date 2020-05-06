from math import ceil
from itertools import permutations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

s = [a, b, c, d, e]

t = []
for i in permutations(list(range(5))):
    c = 0
    for j in range(4):
        c += ceil(s[i[j]] / 10) * 10
    c += s[i[4]]
    t.append(c)

print(min(t))
