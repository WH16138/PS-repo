import sys
sys.setrecursionlimit(100000)

n = int(input())

tree = [[] for i in range(n)]
cost = [[] for i in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
for i in range(n):
    cost[i].extend(map(int,input().split()))

def dfs(parent, bool):
    result = 0
    for child in tree[parent]:
        if child != parent:
            result += dfs(child, not bool)
    return result + cost[parent][int(bool)]

print(min(dfs(0,True),dfs(0,False)))