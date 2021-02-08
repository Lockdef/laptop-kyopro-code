from heapq import heapify, heappush, heappop


def dijkstra(graph, start):  # graphは隣接リスト
    v_size = len(graph)
    dist = [float("inf")] * v_size
    visited = [0] * v_size
    pq = []
    heapify(pq)

    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        cost, u = heappop(pq)
        visited[u] = 1
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            temp_cost = dist[u] + w
            if not visited[v] and temp_cost < dist[v]:
                dist[v] = temp_cost
                heappush(pq, (dist[v], v))
