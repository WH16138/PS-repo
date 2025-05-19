import heapq
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

adj = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def prim(n, adj, start=1):
    visited = [False]*(n+1)
    hq = [(0,start,0)]
    mst_w = 0
    mst = [[] for _ in range(n+1)]
    
    while hq:
        cost,u,p = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        mst_w += cost
        if p != 0:
            mst[u].append((p,cost))
            mst[p].append((u,cost))
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(hq, (w,v,u))
    return mst_w,mst

weight,mst = prim(n,adj)

parent = [0]*(n+1)
dist = [0]*(n+1)
depth = [0]*(n+1)

root = 1
parent[root] = -1
q = deque([root])

while q:
    cur = q.popleft()

    for next, w in mst[cur]:
        if parent[cur] == next:
            continue
        parent[next] = cur
        dist[next] = w
        depth[next] = depth[cur] + 1
        q.append(next)

def max_edge(x,y):
    max_w = 0
    while x != y:
        if depth[x] == depth[y]:
            max_w = max(max_w, dist[x], dist[y])
            x = parent[x]
            y = parent[y]
        elif depth[x] > depth[y]:
            max_w = max(max_w, dist[x])
            x = parent[x]
        else:
            max_w = max(max_w, dist[y])
            y = parent[y]
    return max_w

for _ in range(int(input())):
    x,y = map(int,input().split())
    print(weight - max_edge(x,y))