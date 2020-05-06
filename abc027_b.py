n = int(input())
a = list(map(int, input().split()))
if sum(a) % n != 0:
    print('-1')
else:
    k = sum(a) // n

    left = 0

    right = sum(a)

    temp = 0

    for i in range(n):
