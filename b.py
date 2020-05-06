s = input()

n = len(s)

c = 0

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        c += 1

print(c)
