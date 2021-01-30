n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
r = 0
for i in xy:
    if i[0] < s and i[1] > d:
        print("Yes")
        exit()
print("No")
