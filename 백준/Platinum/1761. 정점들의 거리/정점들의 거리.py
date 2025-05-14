from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

parent = [0]*(n+1)
dist = [0]*(n+1)
depth = [0]*(n+1)

root = 1
parent[root] = -1
q = deque([root])

while q:
    cur = q.popleft()
    for next, w in g[cur]:
        if parent[cur] == next:
            continue
        parent[next] = cur
        dist[next] = w
        depth[next] = depth[cur] + 1
        q.append(next)

m = int(input())

for _ in range(m):
    u,v = map(int,input().split())
    d = 0
    while u != v:
        if depth[u] == depth[v]:
            d += dist[u] + dist[v]
            u = parent[u]
            v = parent[v]
        elif depth[u] > depth[v]:
            d += dist[u]
            u = parent[u]
        else:
            d += dist[v]
            v = parent[v]
    print(d)