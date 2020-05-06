import collections

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    seen = [[False] * w for i in range(h)]

    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    dx = [1, 0, -1, 0, 1, -1, 1, -1]

    def dfs(v):
        stack = collections.deque()
        stack.append(v)
        while stack:
            y, x = stack.pop()
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if not (-1 < ny < h and -1 < nx < w):
                    continue
                if not graph[ny][nx]:
                    continue
                if seen[ny][nx]:
                    continue
                seen[ny][nx] = True
                stack.append([ny, nx])

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not seen[i][j]:
                dfs([i, j])
                count += 1

    print(count)
