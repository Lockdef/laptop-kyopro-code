N = int(input())
a = list(map(int, input().split()))
t = []
for i in range(N):
    t.append([a[i], i])
t.sort(key=lambda x: x[0])
for i in t[::-1]:
    print(i[1] + 1)
