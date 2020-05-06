N = int(input())
print(N // 10 + sum([N // (50 ** i) for i in range(100)]))
