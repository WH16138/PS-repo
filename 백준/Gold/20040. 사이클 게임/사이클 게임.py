import sys
sys.setrecursionlimit(500001)
input = sys.stdin.readline

N,M = map(int,input().split())

par = [i for i in range(N)]

def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        par[py] = px
    else:
        par[px] = py

for i in range(M):
    a, b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        exit()
    union(a, b)
print(0)