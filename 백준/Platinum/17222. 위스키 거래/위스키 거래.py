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

n, m = map(int, input().split())
nmax = list(map(int, input().split()))
mmax = list(map(int, input().split()))
maxF = [float("inf")] + nmax + mmax + [float("inf")]

source = 0
np = source + 1
mp = np + n
sink = mp + m

graph = [[0]*(sink+1) for _ in range(sink+1)]

for i in range(m):
    graph[source][mp+i] = maxF[mp+i]
    flist = list(map(int, input().split()))[1:]
    for f in flist:
        graph[mp+i][f] = maxF[f]

for i in range(n):
    graph[np+i][sink] = maxF[sink]

print(edmonds_karp(graph, source, sink))