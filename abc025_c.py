n = int(input())
b = [int(input()) for _ in range(n-1)]

b.append(0)

print(b)

t = [1] * n

sorted(b)

b = b[:-1]

print(b)

for i in range(1, n):
    print(i)
    if b[i] == b[i-1]:
        t[i] = t[i-1]
    else:
        t[i] = (max(t) + 1 + 1)
    print(f"{i} : {t[i]}")
    print(t)


print(max(t))
