n = int(input())
a, b, c = 0, 0, 1
if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
else:
    for i in range(3, n):
        a, b, c = b, c, (a+b+c) % 10007

    print(c % 10007)
