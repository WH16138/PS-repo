import math
N = int(input())

cost = []

for i in range(N):
    cost.append(list(map(int, input().split())))

dp = [[[-1,-1,-1] for j in range(3)] for i in range(N)]

dp[0][0] = [cost[0][0], math.inf, math.inf]
dp[0][1] = [math.inf, cost[0][1], math.inf]
dp[0][2] = [math.inf, math.inf, cost[0][2]]
for i in range(1,N):
    if i == N-1:
        dp[i][0][0] = math.inf
        dp[i][0][1] = cost[i][1] + min(dp[i-1][0][0], dp[i-1][0][2])
        dp[i][0][2] = cost[i][2] + min(dp[i-1][0][0], dp[i-1][0][1])

        dp[i][1][0] = cost[i][0] + min(dp[i-1][1][1], dp[i-1][1][2])
        dp[i][1][1] = math.inf
        dp[i][1][2] = cost[i][2] + min(dp[i-1][1][0], dp[i-1][1][1])

        dp[i][2][0] = cost[i][0] + min(dp[i-1][2][1], dp[i-1][2][2])
        dp[i][2][1] = cost[i][1] + min(dp[i-1][2][0], dp[i-1][2][2])
        dp[i][2][2] = math.inf
    else:
        dp[i][0][0] = cost[i][0] + min(dp[i-1][0][1], dp[i-1][0][2])
        dp[i][0][1] = cost[i][1] + min(dp[i-1][0][0], dp[i-1][0][2])
        dp[i][0][2] = cost[i][2] + min(dp[i-1][0][0], dp[i-1][0][1])

        dp[i][1][0] = cost[i][0] + min(dp[i-1][1][1], dp[i-1][1][2])
        dp[i][1][1] = cost[i][1] + min(dp[i-1][1][0], dp[i-1][1][2])
        dp[i][1][2] = cost[i][2] + min(dp[i-1][1][0], dp[i-1][1][1])

        dp[i][2][0] = cost[i][0] + min(dp[i-1][2][1], dp[i-1][2][2])
        dp[i][2][1] = cost[i][1] + min(dp[i-1][2][0], dp[i-1][2][2])
        dp[i][2][2] = cost[i][2] + min(dp[i-1][2][0], dp[i-1][2][1])

print(min(sum(dp.pop(),[])))