n = int(input())
t = [int(input()) for _ in range(n)]

min_time = float("inf")

for bit in range(n ** 2):
    a = 0
    b = 0
    for i in range(n):
        if bit & (1 << i):
            a += t[i]
        else:
            b += t[i]
    min_time = min(min_time, max(a, b))

print(min_time)
