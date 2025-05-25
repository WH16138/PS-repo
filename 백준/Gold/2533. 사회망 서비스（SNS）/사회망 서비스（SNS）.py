import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
adj = [[] for i in range(n+1)]

for i in range(n-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[-1,-1] for i in range(n+1)]

def getDP(x,par,pre):
    if dp[x][pre] == -1:
        a = 0
        for v in adj[x]:
            if v != par:
                a += solve(v,x,pre)
        dp[x][pre] = a
    return dp[x][pre]

def solve(x,par,pre):
    if pre == 1:
        return min(1+getDP(x,par,1),0+getDP(x,par,0))
    else:
        return 1+getDP(x,par,1)

print(solve(1,-1,1))