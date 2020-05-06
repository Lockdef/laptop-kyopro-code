n = int(input())
w = list(map(int, input().split()))
a = sum(w) // 2
c = 0
t = []
for i in range(n):
    t.append(abs(sum(w[i:]) - sum(w[:i])))
print(min(t))
