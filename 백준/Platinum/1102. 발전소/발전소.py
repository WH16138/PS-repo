N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
power = [1 if x=='Y' else 0 for x in input()]
P = int(input())

dp = {}
def sol(power1:list):
    if power1.count(1) >= P:
        return 0
    if str(power1) in dp:
        return dp[str(power1)]
    else:
        c = []
        for i,v in enumerate(power1):
            if v:
                for j,v2 in enumerate(power1):
                    if not v2:
                        power2 = power1[:]
                        power2[j] = 1
                        c.append(sol(power2) + cost[i][j])
        dp[str(power1)] = min(c)
        return dp[str(power1)]

if power.count(1) == 0 and P != 0:
    print(-1)
else:
    print(sol(power))