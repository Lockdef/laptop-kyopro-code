s = list(input())
t = list(input())
v = []
if len(s) < len(t):
    print("UNRESTORABLE")
    exit()

for i in range(len(s) - len(t) + 1):
    a = [*s]
    for j in range(len(t)):
        if s[i + j] != t[j] and s[i + j] != '?':
            break
        else:
            a[i + j] = t[j]
    else:
        a = "".join(a)
        a = a.replace('?', 'a')
        v.append(a)

if len(v):
    print(sorted(v)[0])
else:
    print("UNRESTORABLE")
