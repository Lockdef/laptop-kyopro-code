from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append(i + A[i])
    B.append(i - A[i])
C = Counter(B)
S = 0
print(C)
for i in C:
    print(C.items())
    S += i * (i - 1) // 2
print(S)
