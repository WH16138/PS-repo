import heapq as h
import math as m
import sys
input = sys.stdin.readline

BAN = []

def dijkstra(n, adj, s=1):
    dist = [float("inf")] * (n+1) # minimum distance
    dist[s] = 0 # initializing the starting node
    visited = [0] * (n+1) 
    parent = [-1] * (n+1) # route tracking

    que = [(0, s)] # (dist, node)
    while que:
        d, u = h.heappop(que)
        if visited[u]:continue
        visited[u] = 1
        for v, cost in adj[u]:
            if BAN[u][v]:continue
            if d + cost < dist[v]:
                dist[v] = d + cost
                parent[v] = u
                h.heappush(que, (dist[v], v))

    return dist, parent

while 1:
    N,M = map(int,input().split())
    if N + M == 0:break
    S,D = map(int,input().split())

    adj = [[] for _ in range(N)]
    rev = [[] for _ in range(N)]
    for _ in range(M):
        u, v, cost = map(int,input().split())
        adj[u].append((v, cost))
        rev[v].append((u, cost))
    
    BAN = [[0]*N for _ in range(N)]

    dist, p = dijkstra(N,adj,S)

    visited_rev = [0]*N
    que = [D]
    visited_rev[D] = 1

    while que:
        v = que.pop()
        for u, cost in rev[v]:
            if dist[u] + cost == dist[v]:
                BAN[u][v] = 1
                if not visited_rev[u]:
                    visited_rev[u] = True
                    que.append(u)
    
    dist, p = dijkstra(N,adj,S)

    if m.isinf(dist[D]):
        print(-1)
    else:
        print(dist[D])