import sys
sys.setrecursionlimit(200000)

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.w = [0]*(n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        p = self.par[x]
        r = self.find(p)
        self.w[x] += self.w[p]
        self.par[x] = r
        return r

    def weight(self, x):
        self.find(x)
        return self.w[x]

    def diff(self, a, b):
        if self.find(a) != self.find(b):
            return "UNKNOWN"
        return self.weight(b)-self.weight(a)

    def union(self, a, b, d):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        wa = self.weight(a)
        wb = self.weight(b)
        self.par[rb] = ra
        self.w[rb] = wa+d-wb
        
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0: break
    uf = UnionFind(n)
    for _ in range(m):
        q = sys.stdin.readline().split()
        if q[0] == '!':
            a, b, w = map(int, q[1:])
            uf.union(a, b, w)
        else:
            a, b = map(int, q[1:])
            print(uf.diff(a, b))