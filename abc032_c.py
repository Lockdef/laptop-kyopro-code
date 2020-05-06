N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
    exit()
r = 0
ans = 0
tmp = 1
for l in range(N):
    while r < N and tmp * s[r] <= K:
        tmp *= s[r]
        r += 1
    ans = max(ans, r - l)
    if l == r:
        r += 1
    else:
        tmp //= s[l]
print(ans)
