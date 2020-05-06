A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
S = [[], [], []]
for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            S[i].append(1)
        else:
            S[i].append(0)

t = 0


for i in range(3):
    if sum(S[i]) == 3:
        t = 1
    for j in range(3):
        if sum([S[i][j] for i in range(3)]) == 3:
            t = 1
if S[0][0] + S[1][1] + S[2][2] == 3 or S[0][2] + S[1][1] + S[2][0] == 3:
    t = 1

if t:
    print("Yes")
else:
    print("No")
