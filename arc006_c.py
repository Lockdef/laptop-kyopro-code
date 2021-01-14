n = int(input())
w = [int(input()) for _ in range(n)][::-1]
v = [0]
for i in range(n):
    for j in range(len(v)):
        if w[i] >= v[j]:
            v[j] = w[i]
            break
    else:
        v.append(w[i])
print(len(v))
