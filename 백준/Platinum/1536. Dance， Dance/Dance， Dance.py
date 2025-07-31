from collections import deque

def solution(graph, source, sink):
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

N, K = map(int,input().split())

source = 0
man = source + 1
manhate = man + N
woman = manhate + N
womanhate = woman + N
sink = womanhate + N

graph = [[0]*(sink+1) for i in range(sink+1)]

for i in range(N):
    for j,love in enumerate(input()):
        if int(love):
            graph[man+i][woman+j] = 1
        else:
            graph[manhate+i][womanhate+j] = 1
    graph[man+i][manhate+i] = K
    graph[womanhate+i][woman+i] = K

flow = [[0] * len(graph) for _ in range(len(graph))]

round = 0
while round < N:
    for i in range(N):
        graph[source][man+i] += 1
        graph[woman+i][sink] += 1
    max_flow = solution(graph, source, sink)
    if max_flow != N:
        print(round)
        quit()
    round += 1
print(round)