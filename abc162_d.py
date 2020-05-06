N = int(input())
S = input()
a = S.count("R") * S.count("G") * S.count("B")
c = 0
for i in range(N):
    for j in range(i + 1, N):
        k = 2 * j - i
        if k >= N:
            continue
        if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            c += 1
print(a - c)
