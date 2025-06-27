class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, node*2, start, mid)
        right = self.query(l, r, node*2+1, mid+1, end)
        return left + right
    
    def update(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, node*2, start, mid)
            else:
                self.update(idx, val, node*2+1, mid+1, end)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

for t in range(int(input())):
    n,m = map(int, input().split())
    data = [1]*(n)+[0]*m
    pos = [n-i for i in range(n)]
    top = n
    seg_tree = SegmentTree(data)
    seq = list(map(int, input().split()))
    ans = []
    for i in range(m):
        idx = seq[i]
        l = pos[idx-1]-1
        r = n+m-1
        ans.append(seg_tree.query(l+1, r))
        seg_tree.update(l, 0)
        seg_tree.update(top, 1)
        top += 1
        pos[idx-1] = top
    print(*ans)