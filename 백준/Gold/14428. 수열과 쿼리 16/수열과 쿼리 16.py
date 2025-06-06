import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[1e10,-1] for i in range(4*self.n)]
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = [data[start],start]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = min(self.tree[node*2],self.tree[node*2+1])

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return [1e10,-1]
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, node*2, start, mid)
        right = self.query(l, r, node*2+1, mid+1, end)
        return min(left,right)
    
    def update(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.tree[node] = [val, idx]
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, node*2, start, mid)
            else:
                self.update(idx, val, node*2+1, mid+1, end)
            self.tree[node] = min(self.tree[node*2],self.tree[node*2+1])

N = int(input())
numbers = list(map(int,input().split()))

M = int(input())
st = SegmentTree(numbers)
for i in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        st.update(b-1,c)
    if a == 2:
        print(st.query(b-1,c-1)[1]+1)