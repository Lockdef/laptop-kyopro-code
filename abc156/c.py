n = int(input())
x = list(map(int, input().split()))
a = min(x) + (max(x) - min(x)) // 2
s = 1000000000000
for a in range(min(x), max(x)+1):
    s = min(s, sum(map(lambda x: (x - a) ** 2, x)))
print(s)
