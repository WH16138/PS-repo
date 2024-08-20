import heapq as h

N, M = map(int,input().split())

DAG = [[] for i in range(N+1)]
inCount = [0]*(N+1)

for i in range(M):
    u, v = map(int,input().split())
    DAG[u].append(v)
    inCount[v] += 1

def topologicalSort():
    q = []
    result = []
    
    for i in range(1, N+1):
        if inCount[i] == 0:
            h.heappush(q, i)
    
    while q:
        node = h.heappop(q)
        result.append(node)
        
        for nextNode in DAG[node]:
            inCount[nextNode] -= 1
            if inCount[nextNode] == 0:
                h.heappush(q,nextNode)

    return result

print(*topologicalSort())