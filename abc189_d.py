n = int(input())
r = 1
for i in range(n):
    s = input()
    if s == "OR":
        r = r + 2 ** (i + 1)
print(r)
