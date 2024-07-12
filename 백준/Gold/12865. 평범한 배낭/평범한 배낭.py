N,K = map(int,input().split())
item = list(tuple(map(int,input().split())) for _ in range(N))

dp = {}

def search(i,w):
    if dp.get(f'{i} {w}') != None:
        return dp[f'{i} {w}']
    else:
        dp[f'{i} {w}'] = pack(i,w)
        return dp[f'{i} {w}']

def pack(i,w):
    if i == -1:
        return 0
    elif item[i][0] > w:
        return search(i-1,w)
    else:
        return max(item[i][1]+search(i-1,w-item[i][0]), search(i-1,w))

print(pack(N-1,K))