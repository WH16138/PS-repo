V,E = map(int,input().split())

par = list(range(V+1))

def find_par(x):
    if par[x] != x:
        par[x] = find_par(par[x])
    return par[x]

def union_par(x, y):
    x = find_par(x)
    y = find_par(y)
    if x<y:
        par[y] = x
    else:
        par[x] = y

edges = []
for i in range(E):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

min_cost = 0

for edge in edges:
    cost, a, b = edge
    if find_par(a) != find_par(b):
        union_par(a, b)
        min_cost += cost

print(min_cost)