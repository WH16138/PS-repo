A,B,K = map(int,input().split())

p = [x**K for x in range(10)]
dp = [-1]* 3800000
dp[1] = 1

def getNext(n):
    s = 0
    while n:
        s += p[n%10]
        n //= 10
    return s

def solve(n):
    if dp[n] != -1:
        return dp[n]
    
    seq = [n]
    index_map = {n:0}

    var = getNext(n)
    while dp[var] == -1 and var not in index_map:
        seq.append(var)
        index_map[var] = len(seq) - 1
        var = getNext(var)

    if dp[var] != -1:
        minv = dp[var]
        for i in range(len(seq)-1, -1, -1):
            minv = min(minv, seq[i])
            dp[seq[i]] = minv
    else:
        index = index_map[var]

        minv = min(seq[index:])
        for i in range(len(seq)-1, -1, -1):
            if i < index:
                minv = min(minv, seq[i])
            dp[seq[i]] = minv
    
    return dp[n]

ans = 0
for n in range(A,B+1):
    ans += solve(n)

print(ans)