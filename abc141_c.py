n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
p = k - q
s = [p]*n
for i in a:
    s[i-1] += 1

for i in s:
    if i < 1:
        print("No")
    else:
        print("Yes")
