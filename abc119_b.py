n = int(input())
s = [input().split() for _ in [0] * n]
c = 0
for i in s:
    if i[1] == "JPY":
        c += int(i[0])
    else:
        c += float(i[0]) * 380000
print(c)
