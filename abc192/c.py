n, k = map(int, input().split())
for i in range(k):
    n = int("".join((sorted(list(str(n)), reverse=True)))) - \
        int("".join((sorted(list(str(n))))))
print(n)
