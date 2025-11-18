import sys
input = sys.stdin.readline
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1]*(n + 1)
        self.cycle = [0]*(n + 1)
        self.groups = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            self.cycle[ra] = 1
            return True
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.groups -= 1
        return False

    def connected(self):
        return self.groups == 1
    def groupCount(self):
        return self.groups
    def isconnected(self, a, b):
        return self.find(a) == self.find(b)

t = 1
while True:
    n,m = map(int,input().split())
    if n == m == 0:
        break
    uf = UnionFind(n)

    for i in range(m):
        u,v = map(int,input().split())
        uf.union(u,v)
    
    trees = set()
    for i in uf.parent:
        if not uf.cycle[uf.find(i)]:
            trees.add(uf.find(i))
    trees-={0}
    
    if len(trees) > 1:
        print(f"Case {t}: A forest of {len(trees)} trees.")
    if len(trees) == 1:
        print(f"Case {t}: There is one tree.")
    if len(trees) == 0:
        print(f"Case {t}: No trees.")
    t += 1