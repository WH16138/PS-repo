from collections import deque

def edmonds_karp(graph, source, sink):
    flow = [[0] * len(graph) for _ in range(len(graph))]
    max_flow = 0

    while 1:
        parent = [-1] * len(graph)
        que = deque([source])
        while que:
            u = que.popleft()
            for v in range(len(graph)):
                if parent[v] == -1 and graph[u][v] > flow[u][v]:
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
            min_capacity = min(min_capacity, graph[u][v] - flow[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        max_flow += min_capacity

    return max_flow

def char_to_index(c:str):
    return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26

n = int(input())
capacity = [[0] * 52 for _ in range(52)]
for i in range(n):
    u,v,c = input().split()
    capacity[char_to_index(u)][char_to_index(v)] += int(c)
    capacity[char_to_index(v)][char_to_index(u)] += int(c)

print(edmonds_karp(capacity, 0, 25))