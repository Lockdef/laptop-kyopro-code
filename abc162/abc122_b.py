S = input()
acgt = ['A', 'C', 'G', 'T']

c = 0
ans = 0

for i in S:
    if i in acgt:
        c += 1
        ans = max(ans, c)
    else:
        c = 0

print(ans)
