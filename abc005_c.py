t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if n < m:
    print("no")
    exit()
for i in range(n):
    for j in range(len(b)):
        if 0 <= b[j] - a[i] <= t:
            del b[j]
            break

if b:
    print("no")
else:
    print("yes")
