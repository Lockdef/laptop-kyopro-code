h, w = map(int, input().split())
maze = [input() for _ in [0] * (h)]
visited = [[0] * w for _ in [0] * h]
start = [[y, x] for y, row in enumerate(
    maze) for x, elem in enumerate(row) if elem == "s"][0]
goal = [[y, x] for y, row in enumerate(
    maze) for x, elem in enumerate(row) if elem == "g"][0]


def dfs(start, goal, maze, visited, lim_x, lim_y):
    stack = [start]
    visited[start[0]][start[1]] = 1
    while stack:
        x, y = stack.pop(-1)
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x_, y_ = x + i, y + j
            if -1 < x_ < lim_x and -1 < y_ < lim_y and maze[x_][y_] in ["g", "."] and visited[x_][y_] == 0:
                visited[x_][y_] = 1
                stack.append([x_, y_])
    if visited[goal[0]][goal[1]] == 1:
        return "Yes"
    else:
        return "No"


print(dfs(start, goal, maze, visited, h, w))
