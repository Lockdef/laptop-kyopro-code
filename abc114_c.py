n = int(input())
c = 0
for i in range(1, n+1, 2):
    i = set(str(i))
    if len(i) == 3 and '3' in i and '5' in i and '7' in i:
        c += 1
print(c)
