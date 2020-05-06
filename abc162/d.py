N = int(input())
S = input()
c = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if len(set([S[i], S[j], S[k]])) == 3 and j - i != k - j:
                c += 1
print(c)
