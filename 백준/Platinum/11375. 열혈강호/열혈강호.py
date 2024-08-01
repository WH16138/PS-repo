import sys
sys.setrecursionlimit(10000)

N, M = map(int,input().split())

emps = [[]for _ in range(M+1)]
for i in range(N):
    for j in map(int,input().split()[1:]):
        emps[j].append(i)

assign = [-1]*(N+1)
vis = [0]*(N+1)
def dfs(job):
    global vis,assign
    for e in emps[job]:
        if vis[e]:continue
        vis[e] = 1
        if assign[e] == -1 or dfs(assign[e]):
            assign[e] = job
            return True
    return False

def match():
    global vis
    answer = 0
    for job in range(1,M+1):
        vis = [0]*(N+1)
        if dfs(job):answer += 1
    return answer

print(match())