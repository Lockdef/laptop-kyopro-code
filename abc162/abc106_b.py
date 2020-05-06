N = int(input())


def divisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return set(divisors)


c = 0
for i in range(1, N + 1):
    if len(divisors(i)) == 8 and i % 2:
        c += 1

print(c)
