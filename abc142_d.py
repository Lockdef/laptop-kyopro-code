A, B = map(int, input().split())


def gcd(a, b):
    # 最大公約数
    if b == 0:
        return a
    return gcd(b, a % b)
