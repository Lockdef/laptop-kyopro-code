from copy import copy
n = int(input())
s = input()
a = []
for i in range(n-2):
    t = copy(s)
    t = list(s)
    for j in range(n-3):
        t.pop(i)
    a.append(t)
print(len(a))
