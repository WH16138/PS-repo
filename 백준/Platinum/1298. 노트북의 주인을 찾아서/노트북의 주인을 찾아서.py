import sys
sys.setrecursionlimit(10000)

N, M = map(int,input().split())

expect = [[]for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    expect[a].append(b)

assign = [-1]*(N+1)
vis = [0]*(N+1)
def dfs(p):
    global vis,assign
    for laptop in expect[p]:
        if vis[laptop]:continue
        vis[laptop] = 1
        if assign[laptop] == -1 or dfs(assign[laptop]):
            assign[laptop] = p
            return True
    return False

def match():
    global vis
    answer = 0
    for p in range(1,N+1):
        vis = [0]*(N+1)
        if dfs(p):answer += 1
    return answer

print(match())