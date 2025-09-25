import sys
input = sys.stdin.readline
N, M = map(int,input().split())
employeesCanDo = [list(map(int, input().split()))[1:] for _ in range(N)]
employeesCanDo += employeesCanDo[:]

def dfs(e):
    for work in employeesCanDo[e]:
        if visited[work]:
            continue
        visited[work] = True
        if assigned[work] == -1 or dfs(assigned[work]):
            assigned[work] = e
            return True
    return False

visited = [False] * (M + 1)
assigned = [-1] * (M + 1)
result = 0
for e in range(N*2):
    visited = [False] * (M + 1)
    if dfs(e):
        result += 1
print(result)