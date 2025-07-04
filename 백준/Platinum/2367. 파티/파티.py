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

n,k,d = map(int,input().split())

source = 0
Pindex = source + 1
Findex = Pindex + n+1
sink = Findex + d+1

capacity = [[0] * (sink+1) for _ in range(sink+1)]

foodcap = map(int,input().split())
for i,f in enumerate(foodcap,start=1):
    capacity[Findex+i][sink] = f

for i in range(n):
    capacity[source][Pindex+i] = k
    Z = list(map(int,input().split()))
    num = Z[1:]
    for z in num:
        capacity[Pindex+i][Findex+z] = 1

print(edmonds_karp(capacity, source, sink))