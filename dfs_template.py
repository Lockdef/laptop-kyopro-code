seen = []


def dfs(graph, v) {
    seen.append(v)
    for next_v in graph[v]:
        if next_v in seen:
            continue
        dfs(graph, next_v)
}
