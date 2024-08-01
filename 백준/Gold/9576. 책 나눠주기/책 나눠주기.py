import sys
sys.setrecursionlimit(10000)

for t in range(int(input())):

    N, M = map(int,input().split())

    A, wishlist = [[]for _ in range(N)], [[]for _ in range(M)]
    for i in range(M):
        a,b = map(int,input().split())
        wishlist[i] = list(range(a-1,b))
    
    assign = [-1]*N
    vis = [0]*N
    def dfs(student):
        global vis,assign
        for book in wishlist[student]:
            if vis[book]:continue
            vis[book] = 1
            if assign[book] == -1 or dfs(assign[book]):
                assign[book] = student
                return True
        return False
    
    def match():
        global vis
        answer = 0
        for s in range(M):
            vis = [0]*N
            if dfs(s):answer += 1
        return answer
    
    print(match())