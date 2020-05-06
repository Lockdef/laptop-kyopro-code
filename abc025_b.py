n, a, b = map(int, input().split())
s = [input().split() for _ in [0] * n]
c = 0
for i in s:
    if i[0] == "West":
        i[1] *= -1
    if i[1] < a:
        c += a
