n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

temp = [a, b]

for i in p:
    if i in temp:
        print('NO')
        break
    temp.append(i)
else:
    print('YES')
