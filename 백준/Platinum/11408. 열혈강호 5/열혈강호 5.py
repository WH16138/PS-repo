from collections import deque
import sys
input = sys.stdin.readline

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

    while 1:
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

N,M=map(int,input().split())

source = 0
worker = source + 1
work = worker + N
sink = work + M

graph = [[]*(sink+1) for i in range(sink+1)]

for i in range(N):
    worklist = list(map(int,input().split()))
    num = worklist[0]
    worklist = worklist[1:]
    add_edge(graph, source, worker+i, 1, 0)
    for w in range(num):
        add_edge(graph, worker+i, work+worklist[w*2]-1, 1, worklist[w*2+1])

for i in range(M):
    add_edge(graph, work+i, sink, 1, 0)

print("\n".join(map(str,MCMF(graph, source, sink))))