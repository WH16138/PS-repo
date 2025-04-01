class UnionFind():
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.size[x] += self.size[y]
        else:
            self.par[y] = x
            self.rank[x] += 1
            self.size[x] += self.size[y]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def u_size(self, x):
        return self.size[self.find(x)]

for t in range(int(input())):
    F = int(input())
    par = UnionFind(200001)
    n = 0
    hash = {}
    for i in range(F):
        a,b = input().split()
        if a not in hash:
            hash[a] = n
            n += 1
        if b not in hash:
            hash[b] = n
            n += 1
        par.unite(hash[a], hash[b])
        print(par.u_size(hash[a]))