n, m = map(int, input().split())

a = [0] * (n+1)
b = [0] * (n+1)

c = 0

for i in [0]*(m):

    s = input().split()

    if a[int(s[0])] == 0:
        if s[1] == "AC":
            a[int(s[0])] = 1
            c += b[int(s[0])]
        else:
            b[int(s[0])] += 1

print(sum(a), c)
