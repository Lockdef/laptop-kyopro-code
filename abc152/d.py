import numpy as np
n = int(input())
s = []
c = 0
for i in range(1000, 2020):
    for j in range(1000, 2020):
        i = str(i)
        j = str(j)
        if i[0] == j[-1] and i[-1] == j[0] and int(i) <= n and int(j) <= n:
            c += 1

# if n > 100:
#     for i in range(3, len(str(n))):
#         c += 9 * 9 * 10 ** ((i-2) * 2)

#     n = str(n)
#     a = int(n[0])
#     b = int(n[-1])
#     if a <= b:
#         c += np.prod([int(n[i]) for i in range(1, len(n)-1)]) * a
#     else:
#         print(np.prod([int(n[i]) for i in range(1, len(n)-1)]) * a)
#         c += np.prod([int(n[i]) for i in range(1, len(n)-1)]) * a - 1
#     c += (a-1) * (a-1) * 10 ** (2 * (len(n)-2))

print(c)
