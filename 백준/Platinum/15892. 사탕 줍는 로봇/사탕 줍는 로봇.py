from collections import deque
import sys
input = sys.stdin.readline

def edmonds_karp(adj, capacity, source, sink):
    flow = [[0] * len(capacity) for _ in range(len(capacity))]
    max_flow = 0

    while 1:
        parent = [-1] * len(capacity)
        que = deque([source])
        while que:
            u = que.popleft()
            for v in adj[u]:
                if parent[v] == -1 and capacity[u][v] > flow[u][v]:
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
            min_capacity = min(min_capacity, capacity[u][v] - flow[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        max_flow += min_capacity

    return max_flow

N,M = map(int,input().split())

source = 1
sink = N

adj = [[] for _ in range(sink+1)]
capacity = [[0]*(sink+1) for _ in range(sink+1)]

def add_edge(u, v, cap):
    adj[u].append(v)
    adj[v].append(u)
    capacity[u][v] += cap
    capacity[v][u] += cap

for i in range(M):
    u,v,w = map(int,input().split())
    add_edge(u, v, w)

print(edmonds_karp(adj, capacity, source, sink))