N = int(input())
a = N % 1000
if a == 0:
    print(0)
else:
    print(1000 - a)
