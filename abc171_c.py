n = int(input())


def base(x, n):
    result = []
    for i in range(1000):
        x -= 1
        if x / n < 1:
            result.append(x)
            break
        result.append(x % n)
        x //= n

    return result[::-1]


print("".join(map(lambda x: chr(97 + x), base(n, 26))))
