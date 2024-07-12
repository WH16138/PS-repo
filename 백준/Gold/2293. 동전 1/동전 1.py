n, k = map(int, input().split())
coin = sorted(list(set([int(input()) for i in range(n)])))

if k < coin[0]:
    print(0)
    quit()

dp = [1]+[0 for i in range(k)]
for i in range(len(coin)):
    for j in range(coin[i], k+1):
        if (j-coin[i]) >= 0:
            dp[j] += dp[j-coin[i]]
print(dp[k])