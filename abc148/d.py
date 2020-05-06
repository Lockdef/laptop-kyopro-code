n = int(input())
a = list(map(int, input().split()))

temp = 1

count = 0

for i in a:
    if i == temp:
        temp += 1
        count += 1

if temp == 1:
    print(-1)
else:
    print(n - count)
