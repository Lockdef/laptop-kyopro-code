h, w = map(int, input().split())
maze = [input() for _ in [0] * h]
visited = [[0] * w for _ in [0] * h]


def bfs(start, visited, maze, lim_y, lim_x):
    queue = [start]
    visited[start[0]][start[1]] = 1
    distance = {(start[0], start[1]): 0}
    while queue:
        y, x = queue.pop(0)
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            y_, x_ = y + i, x + j
            if -1 < y_ < lim_y and -1 < x_ < lim_x and maze[y_][x_] == '.' and visited[y_][x_] == 0:
                queue.append([y_, x_])
                visited[y_][x_] = 1
                distance[(y_, x_)] = distance[(y, x)] + 1
    return max(distance.values())


max_distance = 0

all_yx = [[j, i] for i in range(w) for j in range(h)]

for start in all_yx:
    if maze[start[0]][start[1]] == '.':
        max_distance = max(max_distance, bfs(
            start, visited, maze, h, w))
        visited = [[0] * w for _ in [0] * h]

print(max_distance)
