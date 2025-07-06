from collections import deque

def edmonds_karp(graph, source, sink):
    flow = [[0] * len(graph) for _ in range(len(graph))]
    max_flow = 0

    while 1:
        parent = [-1] * len(graph)
        que = deque([source])
        while que:
            u = que.popleft()
            for v in range(len(graph)):
                if parent[v] == -1 and graph[u][v] > flow[u][v]:
                    parent[v] = u
                    que.append(v)
                    if v == sink:
                        break

        if parent[sink] == -1:
            break

        min_capacity = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            min_capacity = min(min_capacity, graph[u][v] - flow[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        max_flow += min_capacity

    return max_flow

n,p = map(int,input().split())

source = n+1
sink = 2

capacity = [[0] * (2*n+1) for _ in range(2*n+1)]

for i in range(p):
    u,v = map(int,input().split())
    capacity[n+u][v] += 1
    capacity[v][n+v] = 1

    capacity[n+v][u] += 1
    capacity[u][n+u] = 1


print(edmonds_karp(capacity, source, sink))