import sys, heapq, math
input = sys.stdin.readline

V, E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [math.inf] * (V+1)
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

dist = dijkstra(start)

for i in range(1, V+1):
    if math.isinf(dist[i]):
        print("INF")
    else:
        print(dist[i])