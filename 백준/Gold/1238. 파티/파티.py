import sys, heapq, math
input = sys.stdin.readline

N,M,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [math.inf] * (N+1)
    dist[start] = 0
    que = [(0, start)]
    
    while que:
        cur_dist, cur_node = heapq.heappop(que)
        
        if cur_dist > dist[cur_node]:continue
        
        for next_node, weight in graph[cur_node]:
            next_dist = cur_dist + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(que, (next_dist, next_node))

    return dist

maxdist = 0
for i in range(1,N+1):
    maxdist = max(maxdist, dijkstra(X)[i] + dijkstra(i)[X])

print(maxdist)