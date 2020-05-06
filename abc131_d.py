N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[1])
c = 0
for i in AB:
    c += i[0]
    if c > i[1]:
        print("No")
        exit()
print("Yes")
