L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for i in A:
    if i < L:
        print(L - i)
    elif H < i:
        print(-1)
    else:
        print(0)
