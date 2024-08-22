import sys
sys.setrecursionlimit(9999)

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1,-1,-1] for _ in range(N)]
def sol(n,c):
    if n == N-1:
        return cost[n][c]
    if dp[n][c] == -1:
        a = []
        for i in range(3):
            if i != c:
                a.append(sol(n+1,i))
        dp[n][c] = cost[n][c] + min(a)
    return dp[n][c]

print(min([sol(0,i) for i in range(3)]))