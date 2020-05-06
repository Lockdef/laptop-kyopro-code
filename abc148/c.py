a, b = map(int, input().split())


def f(m, n):
    while (m % n != 0):
        temp = n
        n = m % n
        m = temp
    return n


print(a * b // f(a, b))
