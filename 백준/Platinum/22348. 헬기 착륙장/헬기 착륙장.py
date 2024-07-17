dp = [[0]*50001 for i in range(501)]
mod = 1000000007

# 코드이해 못함 & 이게 왜됨?

dp[1][0] = 1
dp[1][1] = 1
for i in range(500):
    dp[i+1][i+1] = (dp[i+1][i+1]+dp[i][0]) % mod
    dp[i+1][0] = (dp[i+1][0]+dp[i][0]) % mod
    for j in range(1,min(i*(i+1)//2,50000)+1):
        if (i+j)<50000:
            dp[i+1][j+i+1] = (dp[i+1][j+i+1]+dp[i][j])%mod
        dp[i+1][j] = (dp[i+1][j]+dp[i][j])%mod
        dp[i][j] = (dp[i][j]+dp[i][j-1])%mod

for test in range(int(input())):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    answer = 0
    for i in range(501):
        total = i*(i+1)//2
        limit = min(total,a,b)
        if (total - b > limit):
                break
        if (total - b > 0):
            temp = dp[i][limit] - dp[i][total - b - 1]
            if (temp < 0):
                temp += mod
            answer = (answer + temp) % mod
        else:
            answer = (answer + dp[i][limit]) % mod
    print(answer)