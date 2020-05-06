n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
x = 0
n, m, l = [0]*n, [0]*n, [0]*n
k += 1
for i in range(n):
    try:
        print(n, m, l)
        if t[i] == 'r' and n[i] == 0:
            x += p
            n[i+k] = 1
        elif t[i] == 's' and m[i] == 0:
            x += r
            m[i+k] = 1
        elif t[i] == 'p' and l[i] == 0:
            x += s
            l[i+k] = 1
    except IndexError():
        pass


print(x)
