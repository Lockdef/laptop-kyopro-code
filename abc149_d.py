N, K = map(int, input().split())
R, S_, P = map(int, input().split())
T = input()
S = [[] for _ in range(K)]


def f(x):
    if x == "r":
        return P
    if x == "s":
        return R
    if x == "p":
        return S_


for i in range(K):
    S[i].append(T[i])
for i in range(N - K):
    S[i % K].append(T[i + K])
c = 0

for i in range(len(S)):
    t = ""
    for j in range(len(S[i])):
        if t != S[i][j]:
            c += f(S[i][j])
        else:
            S[i][j] = ""
        t = S[i][j]
print(c)
