n = int(input())
a = []
b = []
c = []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append([a_ + b_, a_])
c.sort(reverse=True, key=lambda x: x[0] + x[1])
a_s = sum(a)
b_s = 0
r = 0
for i in c:
    b_s += i[0]
    a_s -= i[1]
    r += 1
    if b_s > a_s:
        break
print(r)
