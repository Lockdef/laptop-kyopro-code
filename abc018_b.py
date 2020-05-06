def f(a, b, s):
    return list(s)[a-1:b][::-1]


s = list(input())
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

for i in l:
    s[i[0] - 1:i[1]] = f(i[0], i[1], s)

print(''.join(s))
