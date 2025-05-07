from math import inf
N = int(input())

dist = [[inf]*N for _ in range(N)]

for y in range(N):
    i = list(map(int,input().split()))
    for x in range(N):
        dist[y][x] = i[x]

for k in range(N):
    for y in range(N):
        for x in range(N):
            dist[y][x] = 1 if any((dist[y][x], dist[y][k] and dist[k][x])) else 0

for i in range(N):
    print(*dist[i])