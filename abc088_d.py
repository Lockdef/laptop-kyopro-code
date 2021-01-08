from collections import deque
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
min_path = [[float("inf") for _ in range(w)] for _ in range(h)]
min_path[0][0] = 1
que = deque([(0, 0)])
count_black = 0
for i in s:
    for j in i:
        if j == '#':
            count_black += 1


while que:
    x, y = que.popleft()
    for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if not (0 <= i <= h - 1 and 0 <= j <= w - 1 and s[i][j] == '.' and min_path[i][j] == float("inf")):
            continue
        min_path[i][j] = min_path[x][y] + 1
        que.append((i, j))


if min_path[h - 1][w - 1] != float("inf"):
    print(h * w - min_path[h - 1][w - 1] - count_black)
else:
    print(-1)
