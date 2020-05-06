a, b, k = map(int, input().split())

s = list(range(a, b+1))
print(*s[:k], sep="\n")
for i in s[-k:]:
    if i not in s[:k]:
        print(i)
