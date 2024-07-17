n, k = map(int, input().split())
coin = sorted(list(set([int(input()) for i in range(n)])))

dp = [1]+[0]*k
for i in range(len(coin)):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]] 
print(dp[k])