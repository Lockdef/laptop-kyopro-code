from collections import defaultdict

n, w = map(int, input().split())
events = defaultdict(int)
for i in range(n):
    s, t, p = map(int, input().split())
    events[s] += p
    events[t] -= p
events = list(events.items())
events.sort(key=lambda x: x[0])
p = 0
for event in events:
    p += event[1]
    if p > w:
        print("No")
        exit()
print("Yes")
exit()
