n, m = map(int, input().split())
node = [[False for _ in range(n)] for _ in range(n)]
edge = [[False for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
ans = 0
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    node[u][v] = True
    node[v][u] = True
    edge[u][v] = False
    edge[v][u] = False


def dfs(u):
    is_cycle = False

    visited[u] = True

    for v in range(n):
        if not node[u][v]:
            continue
        if visited[v] and not edge[u][v]:
            is_cycle = True
            continue
        if not visited[v]:
            edge[u][v] = True
            edge[v][u] = True
            is_cycle |= dfs(v)

    return is_cycle


for i in range(n):
    if not visited[i]:
        if not dfs(i):
            ans += 1

print(ans)
