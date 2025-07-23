from collections import deque
import math
import heapq

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

def widest_path(graph, s, t):
    width = [-1]*len(graph)
    width[s] = math.inf
    pq = [(-math.inf,s)]
    while pq:
        cap, u = heapq.heappop(pq)
        cap = -cap
        if cap < width[u]: continue
        for v, w in enumerate(graph[u]):
            nw = min(cap, w)
            if nw > width[v]:
                width[v] = nw
                heapq.heappush(pq, (-nw, v))
    return width[t]

for t in range(int(input())):
    N,E,A,B = map(int,input().split())

    graph = [[0]*(N+1) for i in range(N+1)]

    for i in range(E):
        u,v,w = list(map(int,input().split()))
        graph[u][v] = w

    print(f"{edmonds_karp(graph, A, B)/widest_path(graph, A, B):.3f}")