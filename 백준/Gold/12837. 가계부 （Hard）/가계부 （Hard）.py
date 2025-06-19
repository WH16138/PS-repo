import sys
input = sys.stdin.readline

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
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1] #sum

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
    
    def Add(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.tree[node] += val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.Add(idx, val, node*2, start, mid)
            else:
                self.Add(idx, val, node*2+1, mid+1, end)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

N,q = map(int, input().split())
arr = [0] * (N+1)
st = SegmentTree(arr)

for _ in range(q):
    op, x, y = map(int, input().split())
    if op == 1:
        st.Add(x-1, y)
    elif op == 2:
        print(st.query(x-1, y-1))
