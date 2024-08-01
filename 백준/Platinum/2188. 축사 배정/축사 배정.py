import sys
sys.setrecursionlimit(10000)

N, M = map(int,input().split())

wishlist = [[]for _ in range(N)]
for i in range(N):
    wishlist[i].extend(list(map(int,input().split()[1:])))

assign = [-1]*(M+1)
vis = [0]*(M+1)
def dfs(cow):
    global vis,assign
    for home in wishlist[cow]:
        if vis[home]:continue
        vis[home] = 1
        if assign[home] == -1 or dfs(assign[home]):
            assign[home] = cow
            return True
    return False

def match():
    global vis
    answer = 0
    for cow in range(N):
        vis = [0]*(M+1)
        if dfs(cow):answer += 1
    return answer

print(match())