from collections import deque

N, M = map(int,input().split())

DAG = [[] for i in range(N+1)]
inCount = [0]*(N+1)

for i in range(M):
    u, v = map(int,input().split())
    DAG[u].append(v)
    inCount[v] += 1

def topologicalSort():
    q = deque()
    result = []
    
    for i in range(1, N+1):
        if inCount[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)
        
        for nextNode in DAG[node]:
            inCount[nextNode] -= 1
            if inCount[nextNode] == 0:
                q.append(nextNode)

    return result

print(*topologicalSort())