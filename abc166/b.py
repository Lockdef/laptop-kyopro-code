N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A += [*list(map(int, input().split()))]
print(N - len(set(A)))
