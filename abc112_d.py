N, M = map(int, input().split())


def divisors(n):
    d = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    return d


d = divisors(M)

ans = 0

for i in d:
    if N * i <= M:
        ans = max(ans, i)

print(ans)
