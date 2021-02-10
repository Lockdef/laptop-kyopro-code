def eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for p in range(2, n + 1):
        if prime[p]:
            for q in range(2 * p, n + 1, p):
                prime[q] = False
    return prime
