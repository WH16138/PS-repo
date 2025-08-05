from collections import deque

class Edge:
    def __init__(self, to, capacity, cost, rev):
        self.to = to
        self.capacity = capacity
        self.cost = cost
        self.rev = rev

def add_edge(graph, u, v, cap, cost):
    graph[u].append(Edge(v, cap, cost, len(graph[v])))
    graph[v].append(Edge(u, 0, -cost, len(graph[u]) - 1))

def MCMF_two(graph, source, sink):
    N = len(graph)
    max_flow = 0
    min_cost = 0


    for _ in range(2):
        parent = [-1] * N
        prev_edge = [-1] * N
        in_que = [False] * N
        in_que[source] = True
        dist = [float("inf")] * N
        dist[source] = 0

        que = deque([source])
        while que:
            u = que.popleft()
            in_que[u] = False
            for i, e in enumerate(graph[u]):
                if e.capacity > 0 and dist[e.to] > dist[u] + e.cost:
                    parent[e.to] = u
                    prev_edge[e.to] = i
                    dist[e.to] = dist[u] + e.cost
                    if not in_que[e.to]:
                        que.append(e.to)
                        in_que[e.to] = True

        if parent[sink] == -1:
            return 0, 0

        min_capacity = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            e = graph[u][prev_edge[v]]
            min_capacity = min(min_capacity, e.capacity)
            v = u

        v = sink
        while v != source:
            u = parent[v]
            e = graph[u][prev_edge[v]]
            e.capacity -= min_capacity
            graph[e.to][e.rev].capacity += min_capacity
            min_cost += e.cost * min_capacity
            v = u

        max_flow += min_capacity

    return max_flow, min_cost

N,M = map(int,input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    u,v,time = map(int,input().split())
    add_edge(graph, u, v, 1, time)
    add_edge(graph, v, u, 1, time)

print(MCMF_two(graph, 1, N)[1])