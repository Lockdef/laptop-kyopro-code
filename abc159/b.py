S = list(input())
N = len(S)
A = S[:(N - 1) // 2]
B = S[(N + 2) // 2:]
if A == A[::-1] and B == B[::-1]:
    print("Yes")
else:
    print("No")
