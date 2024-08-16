N,M = map(int,input().split())

byte_use = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [[0]*(sum(cost)+1) for i in range(N)]

result = sum(cost)
dp[0][0] = 0
dp[0][cost[0]] = byte_use[0]
for i in range(N):
    for c in range(sum(cost)+1):
        dp[i][c] = dp[i-1][c]
        if c >= cost[i]: dp[i][c] = max(dp[i][c],dp[i-1][c-cost[i]] + byte_use[i])
        if dp[i][c] >= M: result = min(result,c)

print(result)