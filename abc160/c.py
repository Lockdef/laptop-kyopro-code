K, N = map(int, input().split())
A = list(map(int, input().split()))
s = []
for i in range(N-1):
    s.append(A[i+1] - A[i])
s.append(A[0] + K - A[-1])
print(K - max(s))
