n, c = map(int, input().split())
events = []
for _ in range(n):
    a, b, c_ = map(int, input().split())
    events.append((a, c_))
    events.append((b + 1, -c_))
events.sort(key=lambda x: x[0])
pre = 0
s = 0
ans = 0
for event in events:
    ans += min(c, s) * (event[0] - pre)
    s += event[1]
    pre = event[0]
print(ans)
