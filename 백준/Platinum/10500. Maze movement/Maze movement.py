from collections import deque
import math

def edmonds_karp(cap, adjlist, source, sink):
    flow = [[0] * len(cap) for _ in range(len(cap))]
    max_flow = 0

    while 1:
        parent = [-1] * len(cap)
        que = deque([source])
        while que:
            u = que.popleft()
            for v in adjlist[u]:
                if parent[v] == -1 and cap[u][v] > flow[u][v]:
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
            min_capacity = min(min_capacity, cap[u][v] - flow[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        max_flow += min_capacity

    return max_flow


N = int(input())
adjlist = [[] for _ in range(N)]
capacity = [[0]*N for _ in range(N)]

def add_edge(u, v, cap):
    adjlist[u].append(v)
    adjlist[v].append(u)
    capacity[u][v] = cap
    capacity[v][u] = cap

room_map = []

maxn = -float("inf")
minn = float("inf")
source = 0
sink = 0
for i in range(N):
    n = int(input())
    if n > maxn:
        maxn = n
        sink = i
    if n < minn:
        minn = n
        source = i
    for j ,other in enumerate(room_map):
        gcd = math.gcd(n, other)
        if gcd > 1:
            add_edge(i, j, gcd)
    room_map.append(n)

print(edmonds_karp(capacity, adjlist, source, sink))