X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)
p += [0] * 1000
q += [0] * 1000
r += [0] * 1000
ans = 0
while X or Y:
    print(X, Y)
    a = r[0]
    if X:
        a = max(a, p[0])
    if Y:
        a = max(a, q[0])
    if X and a == p[0]:
        X -= 1
        p.pop(0)
    elif Y and a == q[0]:
        Y -= 1
        q.pop(0)
    else:
        if Y and p[0] > q[0]:
            Y -= 1
        else:
            X -= 1
        r.pop(0)
    ans += a

print(ans)
