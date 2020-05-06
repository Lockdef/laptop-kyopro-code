n = int(input())
a = map(int, input().split())
c = 0
for i in a:
    while(i % 2 == 0 or i % 3 == 2):
        i -= 1
        c += 1

print(c)
