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

def MCMF(graph, source, sink):
    N = len(graph)
    max_flow = 0
    min_cost = 0

    for i in range(2):
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
            break

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

while True:
    try:
        v, e = map(int, input().split())
    except EOFError:
        break

    graph = [[] for _ in range(v*2)]
    for i in range(v):
        if i == 0 or i == v - 1:
            add_edge(graph, i, i+v, 2, 0)
        else:
            add_edge(graph, i, i+v, 1, 0)
    for _ in range(e):
        a, b, c = map(int, input().split())
        u_out = a - 1
        v_in = b - 1
        add_edge(graph, u_out+v, v_in, 1, c)
    
    flow, cost = MCMF(graph, 0, v*2 - 1)
    print(cost)