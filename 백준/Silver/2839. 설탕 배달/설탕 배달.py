N = int(input())

dp = [-1,-1,-1,1,-1,1]

while len(dp) < N+1:
    if dp[-3] == -1:
        if dp[-5] == -1:
            dp.append(-1)
        else:
            dp.append(dp[-5] + 1)
    elif dp[-5] == -1:
        dp.append(dp[-3] + 1)
    else:
        dp.append(min(dp[-3], dp[-5]) + 1)
    
print(dp[N])