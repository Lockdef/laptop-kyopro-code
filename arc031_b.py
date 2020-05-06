import copy
import collections
s = [list(input()) for _ in range(10)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(v):
    stack = collections.deque()
    stack.append(v)
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (-1 < ny < 10 and -1 < nx < 10):
                continue
            if graph[ny][nx] == "x":
                continue
            if seen[ny][nx]:
                continue
            seen[ny][nx] = True
            stack.append([ny, nx])


for i in range(10):
    for j in range(10):
        seen = [[False] * 10 for _ in range(10)]
        graph = copy.deepcopy(s)

        if graph[i][j] == "o":
            continue
        graph[i][j] = "o"
        count = 0
        for k in range(10):
            for l in range(10):
                if graph[k][l] == "o" and not seen[k][l]:
                    dfs([k, l])
                    count += 1
        if count == 1:
            print("YES")
            exit()

print("NO")
