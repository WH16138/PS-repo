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

N,M,K = map(int,input().split())

source = 0
regular = source + 1
bonus = regular + 1
employee = bonus + 1
work = employee + N
sink = work + M

adj = [[] for _ in range(sink+1)]
capacity = [[0]*(sink+1) for _ in range(sink+1)]

def add_edge(u, v, cap):
    adj[u].append(v)
    adj[v].append(u)
    capacity[u][v] += cap

add_edge(source, regular, N)
add_edge(source, bonus, K)

for e in range(N):
    add_edge(regular, employee + e, 1)
    add_edge(bonus,   employee + e, 1)

for e in range(N):
    data = list(map(int, input().split()))
    for w in data[1:]:
        add_edge(employee + e, work + (w - 1), 1)

for w in range(M):
    add_edge(work + w, sink, 1)


print(edmonds_karp(adj, capacity, source, sink))