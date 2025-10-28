n,k = map(int,input().split())

stuffs = [0]+[list(map(int,input().split())) for _ in range(n)]

DP = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if stuffs[i][0] > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-stuffs[i][0]] + stuffs[i][1])

print(DP[n][k])