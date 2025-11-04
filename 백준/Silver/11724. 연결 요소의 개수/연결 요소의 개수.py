N,M = map(int,input().split())

par = list(range(N))
groups = N

def find(a):
    global par
    if par[a] == a:
        return a
    else:
        par[a] = find(par[a])
        return par[a]

def union(a, b):
    global groups, par
    if find(a) == find(b):
        return False
    else:
        ra = find(a)
        rb = find(b)
        par[rb] = ra
        groups -= 1
        
for i in range(M):
    a,b = map(int,input().split())
    union(a-1,b-1)
print(groups)