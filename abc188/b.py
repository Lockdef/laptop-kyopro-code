n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = sum([a[i] * b[i] for i in range(n)])

if x:
    print("No")
else:
    print("Yes")
