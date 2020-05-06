r, c = map(int, input().split())
start = list(map(lambda x: int(x)-1, input().split()))
goal = list(map(lambda x: int(x)-1, input().split()))
maze = [input() for _ in [0] * r]
visited = [[0] * c for _ in [0] * r]


def bfs(start, goal, maze, visited):
    queue = [start]
    visited[start[0]][start[1]] = 1
    distance = {(start[0], start[1]): 0}
    while queue:
        x, y = queue.pop(0)
        if [x, y] == goal:
            return distance[(x, y)]
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x_, y_ = x + i, y + j
            if maze[x_][y_] == '.' and visited[x_][y_] == 0:
                visited[x_][y_] = 1
                queue.append([x_, y_])
                distance[(x_, y_)] = distance[(x, y)] + 1


print(bfs(start, goal, maze, visited))
