import sys
from collections import deque

N, M, V = map(int,input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    adj[x] = adj[x] + [y]
    adj[y] = adj[y] + [x]

for i,a in enumerate(adj):
    adj[i] = sorted(a)

answer = []
vis = [0]*(N+1)
DFS = [V]
while DFS:
    d = DFS.pop()
    if vis[d]:
        continue
    vis[d] = 1
    answer.append(str(d))
    for x in adj[d][::-1]:
        DFS.append(x)

print(' '.join(answer))

answer = []
vis = [0]*(N+1)
BFS = deque([V])
while BFS:
    b = BFS.pop()
    if vis[b]:
        continue
    vis[b] = 1
    answer.append(str(b))
    for x in adj[b]:
        if not vis[x]:
            BFS.appendleft(x)
            
print(' '.join(answer))