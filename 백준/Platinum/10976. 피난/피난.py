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

for test in range(int(input())):
    N,M = map(int,input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        u,v = map(int,input().split())
        if min(u,v) == 1 or max(u,v) == N:
            graph[min(u,v)][max(u,v)] = 1
        else:
            graph[min(u,v)][max(u,v)] = float("inf")

    source = 1
    sink = N
    print(edmonds_karp(graph, source, sink))