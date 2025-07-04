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

n,m = map(int,input().split())

source = 0
Pindex = source + 1
Bindex = Pindex + n
sink = Bindex + m

capacity = [[0] * (sink+1) for _ in range(sink+1)]

demand = map(int,input().split())
for i,d in enumerate(demand):
    capacity[source][Pindex+i] = d

stock = map(int,input().split())
for i,s in enumerate(stock):
    capacity[Bindex+i][sink] = s

for i in range(m):
    buycap = list(map(int,input().split()))
    for j,b in enumerate(buycap):
        capacity[Pindex+j][Bindex+i] = b

print(edmonds_karp(capacity, source, sink))