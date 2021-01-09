from collections import deque
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
que = deque()
is_end = False
cost = [[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            que.append((i, j))
            cost[i][j] = 0


while que:
    x, y = que.popleft()
    for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if not (0 <= i < h and 0 <= j < w and cost[i][j] == -1):
            continue
        que.append((i, j))
        cost[i][j] = cost[x][y] + 1

max_cost = -1
for i in cost:
    for j in i:
        max_cost = max(max_cost, j)

print(max_cost)
