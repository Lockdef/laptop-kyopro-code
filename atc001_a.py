import sys
sys.setrecursionlimit(100000000)
H, W = map(int, input().split())
c = [input() for i in range(H)]
for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            s = [i, j]
        if c[i][j] == "g":
            g = [i, j]
seen = [[False] * W for _ in range(H)]

ans = "No"

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(v):
    global ans
    y, x = v[0], v[1]
    seen[y][x] = True
    for i in range(4):
        y_ = y + dy[i]
        x_ = x + dx[i]
        if not (0 <= y_ < H and 0 <= x_ < W):
            continue
        if seen[y_][x_]:
            continue
        if c[y_][x_] == "#":
            continue
        if c[y_][x_] == "g":
            print("Yes")
            exit()
        dfs([y_, x_])


dfs(s)

print(ans)
