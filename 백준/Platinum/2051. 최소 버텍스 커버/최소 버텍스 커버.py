import sys
sys.setrecursionlimit(10000)

N, M = map(int,input().split())

Ea = [[]for _ in range(N+1)]
for i in range(N):
    I = input().split()[1:]
    Ea[i+1].extend(list(map(int,I)))

assign = [-1]*(M+1)
vis = [0]*(M+1)
def dfs(a):
    global vis,assign
    for b in Ea[a]:
        if vis[b]:continue
        vis[b] = 1
        if assign[b] == -1 or dfs(assign[b]):
            assign[b] = a
            return True
    return False

def match():
    global vis
    size = 0
    for a in range(1,N+1):
        vis = [0]*(M+1)
        if dfs(a):size += 1
    return size

def alternating_paths(a):
    if a in Xa:
        return
    Xa.add(a)
    for b in Ea[a]:
        if b in Xb or assign[b] == a:
            continue
        if assign[b] != -1:
            Xb.add(b)
            alternating_paths(assign[b])

total_size = match()

A,B,Xa,Xb = set(),set(),set(),set()
for b,a in enumerate(assign):
    if a!= -1:
        A.add(a)
        B.add(b)

for a in range(1,N+1):
    if a not in A:
        alternating_paths(a)

vertex_a = list(set(range(1,N+1)) - Xa)
vertex_b = list(Xb)

print(total_size)
print(len(vertex_a),*vertex_a)
print(len(vertex_b),*vertex_b)