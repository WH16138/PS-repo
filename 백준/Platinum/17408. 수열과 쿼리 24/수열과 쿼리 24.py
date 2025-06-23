import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[0,0] for i in range(4*self.n)]
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = [data[start],0]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = sorted(list(self.tree[node*2]+self.tree[node*2+1]))[-2:]

    def query(self, l, r, ex, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return [0,0]
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, ex, node*2, start, mid)
        right = self.query(l, r, ex, node*2+1, mid+1, end)
        return sorted(list(left+right))[-2:]
    
    def update(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.tree[node] = [val, 0]
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, node*2, start, mid)
            else:
                self.update(idx, val, node*2+1, mid+1, end)
            self.tree[node] = sorted(list(self.tree[node*2]+self.tree[node*2+1]))[-2:]

N = int(input())
arr = list(map(int, input().split()))
st = SegmentTree(arr)
M = int(input())

for _ in range(M):
    q, a, b = map(int, input().split())
    if q == 1:
        st.update(a-1, b)
    elif q == 2:
        print(sum(st.query(a-1, b-1, 0)))