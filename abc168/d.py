N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
rinsetu = [[] for _ in range(N)]
for i in AB:
    rinsetu[i[0] - 1].append(i[1] - 1)
ans = [0 for _ in range(N)]
stack = [*rinsetu[0]]
j = 0
while stack:
    i = stack.pop(0)
    if ans[i] > 0:
        continue
    ans[i] = j + 1
    print(stack)
    stack += rinsetu[i]
    j = i
for i in ans[1:]:
    print("Yes")
    print(i)
