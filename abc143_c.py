n = int(input())
s = input()
ans = 0
if len(set(s)) == 1:
    print(1)
else:
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans+1)
