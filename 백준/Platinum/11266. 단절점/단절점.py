import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(N, adj):
    visi_time = [0] * (N + 1)
    time_low = [0] * (N + 1)
    visited = [False] * (N + 1)
    is_art = [False] * (N + 1)

    time = 0

    def dfs(u, par):
        nonlocal time
        visited[u] = True
        time += 1
        visi_time[u] = time
        time_low[u] = time

        child_count = 0

        for v in adj[u]:
            if not visited[v]:
                child_count += 1
                dfs(v, u)
                time_low[u] = min(time_low[u], time_low[v])
                if par != -1 and time_low[v] >= visi_time[u]:
                    is_art[u] = True
            elif v != par:
                time_low[u] = min(time_low[u], visi_time[v])
        if par == -1 and child_count >=2:
                is_art[u] = True

    for u in range(1, N+1):
        if not visited[u]:
            dfs(u, -1)

    articulation_points = [u for u in range(1, N+1) if is_art[u]]
    return articulation_points

V,E = map(int,input().split())

adj = [[] for _ in range(V+1)]

for e in range(E):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

arts = sol(V, adj)
print(len(arts))
print(*arts)