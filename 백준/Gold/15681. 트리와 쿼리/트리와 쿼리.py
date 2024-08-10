import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N,R,Q = map(int,input().split())

connection = [[] for i in range(N+1)]
subcount = [0]*(N+1)

for i in range(N-1):
    u,v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

def makeTree(curNode, parent):
    subcount[curNode] = 1
    for node in connection[curNode]:
        if node != parent:
            makeTree(node, curNode)
            subcount[curNode] += subcount[node]

makeTree(R, R)

for _ in range(Q):
    u = int(input())
    print(subcount[u])