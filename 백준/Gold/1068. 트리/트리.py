n = int(input())

par = list(map(int,input().split()))

child = [[] for i in range(n)]
for i,p in enumerate(par):
    if p!= -1:
        child[p].append(i)

delnum = int(input())

root = par.index(-1)

def dfs(start):
    if start == delnum: return 0
    a = sum(map(dfs,child[start]))
    return a if a else 1

print(dfs(root))