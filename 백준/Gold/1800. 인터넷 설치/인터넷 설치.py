import sys,heapq,math
input = sys.stdin.readline

n, p, k = map(int,input().split())

gragh = [[]for i in range(n+1)]
for i in range(p):
    a,b,c = map(int, input().split())
    gragh[a].append((b,c))
    gragh[b].append((a,c))

def dijkstra(maxv):
    dist = [[float("inf")]*(k+1) for i in range(n+1)]
    dist[1][k] = 0
    que = [[1,0,0]]
    while que:
        q = heapq.heappop(que)
        node, cost, skip = q
        if node == n:
            continue
        for (next, c) in gragh[node]:
            if c > maxv:
                skip_used = skip + 1
                nextcost = cost
            else:
                skip_used = skip
                nextcost = max(c,cost)
            if skip_used > k:
                continue
            if nextcost < dist[next][skip_used]:
                dist[next][skip_used] = nextcost
                heapq.heappush(que, (next, nextcost, skip_used))
    #print(f"dijk : {min(dist[n])}")
    return min(dist[n])

def binary_search():
    left, right = 1, 1000000
    ans = float("inf")
    while left <= right:
        mid = (left + right) // 2
        #print(f"l:{left} r:{right} c:{costs[mid]}")
        result = dijkstra(mid)
        if math.isinf(result):
            left = mid + 1
        else:
            ans = min(ans, result)
            right = mid - 1
    return -1 if math.isinf(ans) else ans
print(binary_search())