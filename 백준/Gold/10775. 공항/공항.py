from collections import deque

G = int(input())
P = int(input())

g = deque()
for i in range(P):
    g.appendleft(int(input()))

left = G
par = list(range(G+1))

def find(x):
    if par[x]!= x:
        par[x] = find(par[x])
    return par[x]

def union(x,y):
    px, py = find(x), find(y)
    if px < py:
        par[py] = px
    else:
        par[px] = py

while left:
    plane = g.pop()
    target = find(plane)
    if target == 0:
        break
    else:
        union(target, target-1)
        left -= 1
print(G-left)